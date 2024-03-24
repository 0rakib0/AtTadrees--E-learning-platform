from django.shortcuts import render, redirect
from HOD_Dashbord.models import Teacher, User, Subject
from clac.models import Books, Course
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def Teacher_Dashbord(request):
    user = request.user.user_type
    if user == 'teacher':
        teacher = Teacher.objects.all().count()
        students = User.objects.filter(user_type='student').count()
        context = {
            'teacher':teacher,
            'students':students
        }
        return render(request, 'Dashbord/hod_dashbord.html', context)
    else:
        return redirect('error')
@login_required()
def Teacher_View_Books(request):
    user = request.user.user_type
    if user == 'teacher':
        book = Books.objects.all()
        context = {
            'book':book
        }
        return render(request, 'Teacher_dashbord/view_book.html', context)
    else:
        return redirect('error')

@login_required()
def Teacher_view_course(request):
    user = request.user.user_type
    if user == 'teacher':
        course = Course.objects.all().order_by('-id')
        context = {
            'course':course
        }
        return render(request, 'Teacher_dashbord/teacher_view_course.html', context)
    else:
        return redirect('error')
    
@login_required()
def Teacher_Profile(request):
    user = request.user.user_type
    if user == 'teacher':
        teacher = Teacher.objects.get(user=request.user)
        subject = Subject.objects.all()
        context = {
            'teacher':teacher,
            'subject':subject
        }
        return render(request, 'Teacher_dashbord/Teaher_profile.html', context)