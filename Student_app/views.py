from django.shortcuts import render, redirect
from Accounts.models import User
from clac.models import UserCourse, Course, Video, Books, UserBook
from HOD_Dashbord.models import Teacher, Adviser
from django.contrib import messages
from .models import Student_Review, Course_Review
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def Student_dashbord(request):
    course_count = Course.objects.all().count
    user_course_count = UserCourse.objects.filter(user=request.user).count
    user_book_count = UserBook.objects.filter(user=request.user).count
    teacher_count = Teacher.objects.all().count
    advisor_count = Adviser.objects.all().count
    books_count = Books.objects.all().count
    user = request.user.user_type
    if user == 'student':
        context = {
            'course_count':course_count,
            'teacher_count':teacher_count,
            'advisor_count':advisor_count,
            'books_count':books_count,
            'user_course_count':user_course_count,
            'user_book_count':user_book_count
        }
        return render(request, 'Student/stu_dashbord.html', context)
    else:
        return redirect('error')

@login_required()
def Student_profile(request):
    user = request.user.user_type
    if user == 'student':
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            profile_pic = request.FILES.get('profile_pic')
            user = User.objects.get(id=request.user.id)
            print(user)
            if password != '' and password !=None:
                user.set_password(password)
            
            if profile_pic != None:
                user.profile_pic = profile_pic
            user.first_name = first_name
            user.last_name = last_name
                    
            user.save()
            messages.success(request, 'profile Succesfull Udated')
            return redirect('student:student_profile')
        return render(request, 'Student/profile.html')
    else:
        return redirect('error')
    
@login_required()
def MyCourse(request):
    my_courses = UserCourse.objects.filter(user = request.user)
    context = {
        'my_courses':my_courses
    }
    return render(request, 'Student/my_course.html', context)

@login_required()
def Student_Ratings(request):
    if request.method == 'POST':
        review = request.POST.get('review')
        user = request.user
        student_review = Student_Review(
            user = user,
            review_massage = review
        )
        student_review.save()
        messages.success(request, 'Review Submited!')
        return redirect('student:student_dashbord')
    return render(request, 'Student/rating.html')
@login_required()
def Video_Video_playlist(request, slug):
    course = Course.objects.filter(slug=slug)
    course_id = Course.objects.get(slug=slug)
    lecture = request.GET.get('lecture')
    revies = Course_Review.objects.filter(course = course_id)
    video = None
    if lecture:
        video = Video.objects.get(id=lecture)
    if course.exists():
        course = course.first()
    else:
        return redirect('404')
    context = {
       'course':course,
       'video':video,
       'revies':revies,
    }
    return render(request, 'Student/video_plylist.html', context)

@login_required()
def My_book(request):

    my_course = UserBook.objects.filter(user=request.user)
    
    context = {
       'my_course':my_course 
    }
    return render(request, 'Student/my_book.html', context)