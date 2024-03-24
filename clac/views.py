from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from HOD_Dashbord.models import *
from clac.models import Category, Course, Lesson, Video, Whats_learn, Requierment, Books, Languege, UserCourse, Contact_Us, UserBook
from .import views
from Student_app.models import Course_Review, Student_Review
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests
from ast import Str
import json
import requests
# Create your views here.


def homepage(request):
    teachers = Teacher.objects.all()
    student_review = Student_Review.objects.all()
    categorys = Category.objects.all()[0:8]
    courses = Course.objects.filter(publish_satatus=True)[0:5]
    adviser = Adviser.objects.all()
    context = {
        'teacher':teachers,
        'adviser':adviser,
        'categorys':categorys,
        'courses':courses,
        'student_review':student_review
    }
    return render(request,'home/index.html', context)


def Course_list(request):
    course = Course.objects.filter(publish_satatus=True)[0:5]
    catagory_id = request.GET.get('category')
    all_course = Course.objects.filter(publish_satatus=True)
    course_by_category = Course.objects.filter(category=catagory_id)
    print(catagory_id)
    category = Category.objects.all()
    context = {
        'course':course,
        'category':category,
        'all_course':all_course,
        'course_by_category':course_by_category
    }
    return render(request, 'home/course_list.html', context)


def Single_course_page(request, slug):
    time_duration = None
    check_enroll = None
    check_review = None
    course = Course.objects.get(slug=slug)
    catagory_ID = course.category.id
    releted_course = Course.objects.filter(category=catagory_ID, publish_satatus=True)[:5]
    corse_id = course.id
    video = Video.objects.filter(course=corse_id)
    whats_learn = Whats_learn.objects.get(course=corse_id)
    requirment = Requierment.objects.get(course=corse_id)
    time_duration = Video.objects.filter(course__slug=slug).aggregate(sum=Sum('time_duration'))

    review_rating_5 = Course_Review.objects.filter(course=course, rating=5).count()
    review_rating_4 = Course_Review.objects.filter(rating=4, course=course).count()
    review_rating_3 = Course_Review.objects.filter(rating=3, course=course).count()
    review_rating_2 = Course_Review.objects.filter(rating=2, course=course).count()
    review_rating_1 = Course_Review.objects.filter(rating=1, course=course).count()
    all_review = Course_Review.objects.filter(course=course)
    count_review = Course_Review.objects.filter(course=course).count()
   

    if request.user.is_authenticated:
        check_review = Course_Review.objects.filter(user = request.user, course=course)

    try:
        if request.user.is_authenticated:
            check_enroll = UserCourse.objects.filter(user=request.user, course=course)
    except UserCourse.DoesNotExist:
        check_enroll = None
    context = {
        'course':course,
        'whats_learn':whats_learn,
        'requirment':requirment,
        'releted_course':releted_course,
        'time_duration':time_duration,
        'check_enroll':check_enroll,
        'check_review':check_review,
        'review_rating_5':review_rating_5,
        'review_rating_4':review_rating_4,
        'review_rating_3':review_rating_3,
        'review_rating_2':review_rating_2,
        'review_rating_1':review_rating_1,
        'all_review':all_review,
        'count_review':count_review
    }

    return render(request, 'home/single_course.html', context)

def Book(request):
    book_list = Books.objects.filter(is_published=True)
    context = {
        'book_list':book_list
    }
    return render(request, 'home/view_book.html', context)

def View_single_Book(request, id):
    book  = Books.objects.get(id=id)
    return render(request, 'home/single_book.html', context={'book':book})


def Error(request):
    return render(request, 'home/error.html')



# =======================> Categorey <========================
@login_required()
def Add_category(request):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        if request.method == 'POST':
            category_name = request.POST.get('category_name')
            print(category_name)

            category = Category(
                name = category_name
            )
            category.save()
            messages.success(request, 'Category Successfully save!')
            return redirect('add_category')
        return render(request, 'home/add_category.html')
    else:
        return redirect('error')

@login_required()
def View_category(request):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        categorys = Category.objects.all()
        context = {
            'categorys':categorys
        }
        return render(request, 'home/view_category.html', context)
    else:
        return redirect('error')

@login_required()  
def Updat_category(request, id):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        category = Category.objects.get(id=id)
        if request.method == 'POST':
            category_name = request.POST.get('category_name')
            category = Category.objects.get(id=id)
            category.name = category_name
            category.save()
            messages.success(request, 'Category Successfully Updated!')
            return redirect('view_category')
        context = {
            'category':category
        }
        return render(request, 'home/update_category.html', context)
    else:
        return redirect('error')
    

@login_required()
def Delete_Category(request, id):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        category = Category.objects.get(id=id)
        category.delete()
        messages.success(request, 'Category Successfully Delete!')
        return redirect('view_category')
    else:
        return redirect('error')
    

    
# =======================> Language <========================

@login_required()
def Add_Languege(request):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        if request.method == 'POST':
            language_name = request.POST.get('language_name')
            language = Languege(
                languege_name = language_name
            )
            language.save()
            messages.success(request, 'New Kanguage Added!')
            return redirect ('add_language')
        return render(request, 'home/add_languege.html')
    else:
        return redirect('error')

@login_required()  
def View_language(request):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        languages = Languege.objects.all()
        context = {
            'languages':languages
        }
        return render(request, 'home/view_language.html', context)
    else:
        return redirect('error')


@login_required()
def Delete_Language(request, id):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        language = Languege.objects.get(id=id)
        language.delete()
        messages.success(request, 'Language Successfully Delete!')
        return redirect('view_language')
    else:
        return redirect('error')
    

# ==========================> Course <======================

@login_required()
def Add_Course(request):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        languages = Languege.objects.all()
        categorys = Category.objects.all()
        if request.method == 'POST':
            course_name = request.POST.get('course_name')
            course_title = request.POST.get('course_title')
            course_video = request.POST.get('course_video')
            language = request.POST.get('language')
            category = request.POST.get('category')
            deadline = request.POST.get('deadline')
            description = request.POST.get('description')
            course_img = request.FILES.get('course_img')
            regular_price = request.POST.get('regular_price')
            discount_price = request.POST.get('discount_price')
            skill_level = request.POST.get('skill_level')
            certificate = request.POST.get('certificate')

            lang = Languege.objects.get(id=language)
            cat = Category.objects.get(id=category)

            if Course.objects.filter(title = course_title).first():
                messages.warning(request, 'Same Title Already Exist! Please Try Defrent.')
                return redirect('add_course')
            if language == 'SELECT LANGUAGE' or language == None:
                messages.warning(request, 'Language Must Be select!')
                return redirect('add_course')
            if category == 'SELECT CATEGORY' or category == None:
                messages.warning(request, 'Category Must Be select!')
                return redirect('add_course')
            course = Course (
                title_1 = course_name,
                title = course_title,
                course_video = course_video,
                languege = lang,
                category = cat,
                description = description,
                course_image = course_img,
                price = regular_price,
                discount = discount_price,
                skill_level = skill_level,
                certificate = certificate,
            )
            if deadline:
                course.deadline=deadline
            if user_ == 'admin':
                course.publish_satatus = True
            course.save()
            messages.success(request, 'Course Successfully Added!')
            return redirect('whats_learn')
        context = {
          'language':languages,
          'category':categorys 
        }
        return render(request, 'home/add_course.html', context)
    else:
        return redirect('error')

@login_required()
def Purlish_course(request, id):
    user_= request.user.user_type
    if user_ == 'admin':
        course = Course.objects.get(id=id)
        course.publish_satatus = True
        course.save()
        return redirect('view_course')
    else:
        return redirect('error')


@login_required()   
def View_course(request):
    user_= request.user.user_type
    if user_ == 'admin':
        courses = Course.objects.all().order_by('-id')
        context = {
            'courses':courses
        }
        return render(request, 'home/view_course.html', context)
    else:
        return redirect('error')



@login_required()   
def Update_course(request, id):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        course = Course.objects.get(id=id)
        laguage = Languege.objects.all()
        category = Category.objects.all()
        if request.method == 'POST':
            course_name = request.POST.get('course_name')
            course_title = request.POST.get('course_title')
            course_video = request.POST.get('course_video')
            language = request.POST.get('language')
            category = request.POST.get('category')
            deadline = request.POST.get('deadline')
            description = request.POST.get('description')
            course_img = request.FILES.get('course_img')
            regular_price = request.POST.get('regular_price')
            discount_price = request.POST.get('discount_price')
            skill_level = request.POST.get('skill_level')
            certificate = request.POST.get('certificate')

            lang = Languege.objects.get(id=language)
            cat = Category.objects.get(id=category)

            course = Course.objects.get(id=id)
            course.title_1 = course_name
            course.title = course_title
            course.course_video = course_video
            course.languege = lang
            course.category = cat
            if deadline:
                course.deadline = deadline
            course.description = description
            course.course_image = course_img
            course.price = regular_price
            course.discount = discount_price
            course.skill_level = skill_level
            course.certificate = certificate
            course.save()
            messages.success(request, 'Course Successfully Updated!')
            return redirect('view_course')
        context = {
            'course':course,
            'laguage':laguage,
            'category':category
        }
        return render(request, 'home/update_course.html', context)
    else:
        return redirect('error')
    


@login_required()
def Delete_course(request, id):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        course = Course.objects.get(id=id)
        course.delete()
        messages.success(request, 'Course Successfully Deleted!')
        return redirect('view_course')
    else:
        return redirect('error')
    

# ==========================> Whats learn <========================

@login_required()
def Whats_learn_from_course(request):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        course_first = Course.objects.last()
        if request.method == 'POST':
            point1 = request.POST.get('point1')
            point2 = request.POST.get('point2')
            point3 = request.POST.get('point3')
            point4 = request.POST.get('point4')
            point5 = request.POST.get('point5')
            point6 = request.POST.get('point6')
            point7 = request.POST.get('point7')
            course_id = request.POST.get('course_id')

            cors = Course.objects.get(id=course_id)

            whats_learn=Whats_learn(
                course = cors,
                pont1 = point1,
                pont2 = point2,
                pont3 = point3,
                pont4 = point4,
                pont5 = point5,
                pont6 = point6,
                pont7 = point7
            )

            whats_learn.save()
            return redirect('add_course_requirment')

        context = {
            'course_first':course_first
        }
        return render(request, 'home/whats_learn.html', context)

    else:
        return redirect('error')
    
def View_whats_learn(request):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        whats_learn = Whats_learn.objects.all()
        return render(request, 'home/view_whats_learn.html', context={'whats_learn':whats_learn})
    else:
        return redirect('error')
    
def Update_whats_learn(request, id):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        if request.method == 'POST':
            point1 = request.POST.get('point1')
            point2 = request.POST.get('point2')
            point3 = request.POST.get('point3')
            point4 = request.POST.get('point4')
            point5 = request.POST.get('point5')
            point6 = request.POST.get('point6')
            point7 = request.POST.get('point7')

            whats_learn = Whats_learn.objects.get(id=id)
            whats_learn.pont1 = point1
            whats_learn.pont2 = point2
            whats_learn.pont3 = point3
            if point4 !='' or point4 !=None:
                whats_learn.pont4 = point4

            if point5 !='' or point5 !=None:
                whats_learn.pont5 = point5

            if point6 !='' or point6 !=None:
                whats_learn.pont6 = point6

            if point7 !='' or point7 !=None:
                whats_learn.pont7 = point7

            whats_learn.save()
            messages.success(request, 'Successfully Updated!')
            return redirect('view_whats_learn')


        whats_learn = Whats_learn.objects.get(id=id)
        return render(request, 'home/whats_learn_update.html', context={'whats_leanr':whats_learn })
    else:
        return redirect('error')


# ==========================> Course Requirment <========================


def Add_cours_requirment(request):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        if request.method == 'POST':
            point1 = request.POST.get('point1')
            point2 = request.POST.get('point2')
            point3 = request.POST.get('point3')
            course_id = request.POST.get('course_id')

            cors = Course.objects.get(id=course_id)

            course_requirment = Requierment (
                point_1 = point1,
                point_2 = point2,
                point_3 = point3,
                course = cors
            )
            course_requirment.save()
            messages.success(request, 'Course successfully Saved!')
            if user_ == 'admin':
                return redirect('view_course')
            elif user_ == 'teacher':
                return redirect('Teacher_ap:teacher_view_course')

        course_first = Course.objects.last()
        context = {
            'course_first':course_first
        }
        return render(request, 'home/add_course_requirment.html', context)
    
    else:
        return redirect('error')
    

def View_course_requirment(request):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        requirment = Requierment.objects.all().order_by('-id')
        context = {
            'requirment':requirment
        }
        return render(request, 'home/view_course_requirment.html', context)
    
    else:
        return redirect('error')
    
def Update_course_requirment(request, id):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        if request.method == 'POST':
            point1 = request.POST.get('point1')
            point2 = request.POST.get('point2')
            point3 = request.POST.get('point3')

            requirment = Requierment.objects.get(id=id)
            requirment.point_1 = point1
            if point2 != '' or point2 != None:
                requirment.point_2 = point2

            if point3 != '' or point3 != None:
                requirment.point_3 = point3
            requirment.save()
            messages.success(request, 'Successfully Updated!')
            return redirect('view_course_requirment')
        requirments = Requierment.objects.get(id=id)
        course_first = Course.objects.last()
        context = {
            'requirments':requirments,
            'course_first':course_first
        }
        return render(request, 'home/update_requirment.html', context)
    else:
        return redirect('error')
    
# ==========================> Lessone <================================


def Add_lesson(request):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        if request.method == 'POST':
            course_id = request.POST.get('course_id')
            lesson_name = request.POST.get('lesson_name')

            crs = Course.objects.get(id=course_id)
            
            lesson = Lesson(
                course = crs,
                name = lesson_name
            )
            lesson.save()
            messages.success(request, 'Lesson Successfully Add!')
            return redirect('add_lesson')
        course = Course.objects.all().order_by('-id')
        context = {
            'course':course
        }
        return render(request, 'home/add_lesson.html', context)
    else:
        return redirect('error')
    
def View_leson(request):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        lessone = Lesson.objects.all().order_by('-id')
        return render(request, 'home/view_lesson.html', context={'lessone':lessone})
    else:
        return redirect('error')

    
def Update_Lesson(request, id):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        lesson = Lesson.objects.get(id=id)
        if request.method == 'POST':
            course_id = request.POST.get('course_id')
            lesson_name = request.POST.get('lesson_name')
            crs = Course.objects.get(id=course_id)
            lesson.course = crs
            lesson.name = lesson_name

            lesson.save()
            messages.success(request, 'Lesson Updated!')
            return redirect('view_lesson')
        context = {
            'lesson':lesson
        }
        return render(request, 'home/update_lesson.html', context)
    else:
        return redirect('error')
def Delete_lesson(request, id):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        lesson = Lesson.objects.get(id=id)
        lesson.delete()
        messages.success(request, 'Lesson Successfully Delete!')
        return redirect('view_lesson')
    else:
        return redirect('error')
    

# ==========================> Course Video <================================

def Add_Video(request):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        course_id = None
        context = None
        if request.method == 'GET':
            course_id = request.GET.get('course_id')
        elif request.method == 'POST':
            course_id = request.GET.get('course_id')
        course_id = course_id
        print(course_id)
        if course_id == None:
            course = Course.objects.all().order_by('-id')
            context = {
                'course':course,
            }
            return render(request, 'home/cours_id.html', context)
        else:
            course = Course.objects.get(id=course_id)
            lesson = Lesson.objects.filter(course = course_id)
            if request.method == 'POST':
                serial_number = request.POST.get('serial_number')
                thumbnail = request.FILES.get('thumbnail')
                title = request.POST.get('title')
                youtube_id = request.POST.get('youtube_id')
                time_duration = request.POST.get('time_duration')
                courses_id = request.POST.get('course_id')
                lessone_id = request.POST.get('lessone_id')
                is_preview = request.POST.get('is_preview')
                

                leson = Lesson.objects.get(id=lessone_id)
                crs = Course.objects.get(id=courses_id)

                video = Video(
                    serial_number = serial_number,
                    thumbnail = thumbnail,
                    title = title,
                    youtube_id = youtube_id,
                    time_duration = time_duration,
                    course = crs,
                    lesson = leson
                )
                if is_preview == True:
                   video.preview = True
                video.save()
                messages.success(request, 'Video Successfully Added!')
                return redirect('add_video')
            context = {
                'course':course,
                'lesson':lesson,
            }
            return render(request, 'home/add_video.html', context)
    else:
        return redirect('error')

def View_Video(request):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        videos = Video.objects.all().order_by('-id')
        context = {
            'videos':videos
        }
        return render(request, 'home/view_video.html', context)
    else:
        return redirect('index')
    
def Delete_video(request, id):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        video = Video.objects.get(id=id)
        video.delete()
        messages.success(request, 'Video Successfully deleted!')
        return redirect('view_video')




# ========================> ENROLL COURSE <=======================
@login_required()
def Checkout(request, slug):
    payment_url = None
    course = Course.objects.get(slug=slug)
    action = request.GET.get('action')
    if course.price == 0:
        course = UserCourse(
            user = request.user,
            course = course,
        )
        course.save()
        return redirect('student:my_course')
    else:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            country = request.POST.get('country')
            address_1 = request.POST.get('address_1')
            address_2 = request.POST.get('address_2')
            city = request.POST.get('city')
            postcode = request.POST.get('postcode')
            phone = request.POST.get('phone')
            order_comments = request.POST.get('order_comments')
            if course.discount == 0:
                amount = course.price
            else:
                amount = course.discount
            
            
            payload = {
                "store_id": 'merchantid',
                "tran_id": 'A205220',
                "success_url": request.build_absolute_uri('/payment-success/'),
                "fail_url": request.build_absolute_uri('/payment-faild/'),
                'cancel_url': request.build_absolute_uri('/payment-faild/'),
                "amount": 10 or 10.50 or 10.6,
                "currency": "BDT",
                "signature_key": 'dc0c2802bf04d2ab3336ec21491146',
                "cus_name": first_name,
                "cus_last_name": last_name,
                "cus_email": email,
                "cus_add1":address_1,
                "cus_add2":address_2,
                "cus_city": city,
                # "cus_state":stat,
                "cus_postcode": postcode,
                "cus_country": country,
                "cus_phone": phone,
                'desc':order_comments,
            }
            url = 'https://sandbox.aamarpay.com/request.php'
            tracking_url = "https://sandbox.aamarpay.com/paynow.php?track=AAM1684348081103870"
            response = requests.post(url, data=payload)
            response = requests.get(tracking_url)
            # payment_url = response.json().get('url')

            if response.status_code == 200:
                print('----------------------------------')
                payment_info = response.text
                # Process the payment information as needed
                # Render the payment form with the Aamarpay gateway URL and form data
                return render(request, 'payment.html', {'gateway_url': settings.AAMARPAY_GATEWAY_URL, 'form_data': response.text})
            else:
                # Handle error
                return render(request, 'error.html', {'error_message': 'Failed to connect to Aamarpay'})
            
        # when payment success
        # user_course = UserCourse(
        #     user = request.user,
        #     course = course,
        #     paid = True
        # )
        # user_course.save()
        # return redirect('student:my_course')
           
    return render(request, 'home/checkout.html', context={'course':course, 'payment_url':payment_url})


def Book_checkout(request, id):
    payment_url = None
    book = Books.objects.get(id=id)
    action = request.GET.get('action')
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        address_1 = request.POST.get('address_1')
        address_2 = request.POST.get('address_2')
        city = request.POST.get('city')
        postcode = request.POST.get('postcode')
        phone = request.POST.get('phone')
        order_comments = request.POST.get('order_comments')


        if book.discount_price == 0:
            amount = book.regular_price
        else:
            amount = book.discount_price
        
        
        payload = {
            "store_id": 'aamarpaytest',
            "tran_id": 'eew',
            "success_url": request.build_absolute_uri('/payment-success/'),
            "fail_url": request.build_absolute_uri('/payment-faild/'),
            'cancel_url': request.build_absolute_uri('/payment-faild/'),
            "amount": amount,
            "currency": "BDT",
            "signature_key": 'dbb74894e82415a2f7ff0ec3a97e4183',
            "desc": order_comments,
            "cus_name": first_name,
            "cus_last_name": last_name,
            "cus_email": email,
            "cus_add1":address_1,
            "cus_add2":address_2,
            "cus_city": city,
            # "cus_state":stat,
            "cus_postcode": postcode,
            "cus_country": country,
            "cus_phone": phone,
            'desc':order_comments,
        }
        url = 'https://sandbox.aamarpay.com/request.php'
        tracking_url = "https://sandbox.aamarpay.com/paynow.php?track=AAM1684348081103870"
        response = requests.post(url, data=payload)
        response = requests.get(tracking_url)
        # payment_url = response.json().get('url')

        if response.status_code == 200:
            print('----------------------------------')
            payment_info = response.text
            # Process the payment information as needed
            # Render the payment form with the Aamarpay gateway URL and form data
            return render(request, 'payment.html', {'gateway_url': settings.AAMARPAY_GATEWAY_URL, 'form_data': response.text})
        else:
            # Handle error
            return render(request, 'error.html', {'error_message': 'Failed to connect to Aamarpay'})


    # when payment success
        # user_book = UserBook(
        #     user = request.user,
        #     book = book,
        #     paid = True
        # )
        # user_book.save()
        # return redirect('student:my_book')





    return render(request, 'home/book_checkout.html', context={'book':book, 'payment_url':payment_url})




@login_required()
def Course_Reviews(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        review_title = request.POST.get('review_title')
        course_id = request.POST.get('course_id')
        review_massage = request.POST.get('review_massage')

        user = request.user
        course = Course.objects.get(id=course_id)
        review = Course_Review(
            user = user,
            course = course,
            review_title = review_title,
            review_massage = review_massage,
            rating = rating
        )

        review.save()
        # return HttpResponseRedirect(reverse('single_course', kwargs='slug' ))
        
    
    return redirect('index')

def Contact_Use(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        messge = request.POST.get('message')

        contact_us = Contact_Us(
            name = name,
            email = email,
            message = messge
        )
        contact_us.save()
        return redirect('contact_us')
    return render(request, 'home/contact_us.html')

@login_required()
def payment_success(request):
    
    return render(request, 'home/success.html')
@login_required()
def payment_failure(request):
    return render(request, 'home/failure.html')