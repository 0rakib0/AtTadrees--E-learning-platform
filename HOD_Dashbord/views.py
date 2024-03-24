from django.shortcuts import render, redirect
from .models import Teacher, Adviser, Subject
from clac.models import Contact_Us, Course, UserBook
from Accounts.models import User
from django.contrib import messages
import random
from clac.models import Books
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def Dashbord(request):
    user = request.user
    if user.user_type == 'teacher' or user.user_type == 'admin':
        course_count = Course.objects.all().count()
        book_count = Books.objects.all().count()
        teacher = Teacher.objects.all().count()
        students = User.objects.filter(user_type='student').count()
        context = {
            'teacher':teacher,
            'students':students,
            'course_count':course_count,
            'book_count':book_count
        }
        return render(request, 'Dashbord/hod_dashbord.html', context)
    else:
        return redirect('error')

@login_required()
def Add_teacher(request):
    user = request.user
    if user.user_type == 'admin':
        subject = Subject.objects.all()
        if request.method == 'POST':
            first_name     = request.POST.get('first_name')
            last_name      = request.POST.get('last_name')
            gender         = request.POST.get('gender')
            title          = request.POST.get('title')
            date_of_birth  = request.POST.get('dob')
            mobile         = request.POST.get('mobile')
            joine_date     = request.POST.get('join_date')
            profile_pic    = request.FILES.get('profile_pic')
            email          = request.POST.get('email')
            password1      = request.POST.get('password1')
            password2      = request.POST.get('password2')
            address        = request.POST.get('address')
            city           = request.POST.get('city')
            state          = request.POST.get('state')
            zipe_code      = request.POST.get('zipe_code')
            country        = request.POST.get('country')
            subject        = request.POST.get('subject')
            rendom_int = random.randint(0, 1000)
            randon_str = str(rendom_int)
            teacher_id     = 'TCH'+randon_str


            if first_name =='':
                messages.warning(request, 'First name must be set')
                return redirect('hod:add_teacher')
            
            if last_name=='':
                messages.warning(request, 'Last name must be set')
                return redirect('hod:add_teacher')
            
            if email=='':
                messages.warning(request, 'Email must be set')
                return redirect('hod:add_teacher')
            
            if password1 =='' or password2=='':
                messages.warning(request, 'Password must be set')
                return redirect('hod:add_teacher')
            

            if User.objects.filter(email = email).first():
                messages.warning(request, 'Email Already Exist!')
                return redirect('hod:add_teacher')
            
            if password1 != password2:
                messages.warning(request,'2 Password Not Match!')
                return redirect('hod:add_teacher')
            else:
                user = User(
                    first_name   = first_name, 
                    last_name    = last_name,
                    email        = email,
                    profile_pic  = profile_pic,
                    user_type    = 'teacher'
                )
                user.set_password(password1)
                user.save()

                teacher = Teacher(
                    user        = user,
                    gender      = gender,
                    DOB         = date_of_birth,
                    Joine_date  = joine_date,
                    address     = address,
                    city        = city,
                    state       = state,
                    country     = country,
                    zipe_code   = zipe_code,
                    phone_number= mobile,
                    teacher_id  = teacher_id,
                    subject     = subject,
                    title       = title,
                )
                teacher.save()
                messages.success(request, 'Teacher successfully created')
                return redirect('hod:add_teacher')
        return render(request, 'Dashbord/Add_teacher.html', context={'subject':subject})
    else:
        return redirect('error')

@login_required()
def View_Teacher(request):
    user = request.user
    if user.user_type == 'admin':
        teacher = Teacher.objects.all()
        context = {
            'teachers':teacher
        }
        return render(request, 'Dashbord/view_teacher.html', context)
    return redirect('error')
@login_required()
def Edit_Teacher(request, id):
    user = request.user
    if user.user_type == 'admin':
        subject = Subject.objects.all()
        if request.method == 'POST':
            teacher_id     = request.POST.get('teacher_id')
            first_name     = request.POST.get('first_name')
            last_name      = request.POST.get('last_name')
            title          = request.POST.get('title')
            gender         = request.POST.get('gender')
            date_of_birth  = request.POST.get('dob')
            mobile         = request.POST.get('mobile')
            joine_date     = request.POST.get('join_date')
            profile_pic    = request.FILES.get('profile_pic')
            password1      = request.POST.get('password1')
            address        = request.POST.get('address')
            city           = request.POST.get('city')
            state          = request.POST.get('state')
            zipe_code      = request.POST.get('zipe_code')
            country        = request.POST.get('country')
            subject        = request.POST.get('subject')

            user = User.objects.get(id=teacher_id)
            user.first_name = first_name
            user.last_name = last_name
            if profile_pic !=None and profile_pic !='':
                user.profile_pic = profile_pic
            
            if password1 !=None and password1 !='':
                user.set_password(password1)

            user.save()

            teacher = Teacher.objects.get(user=teacher_id)

            teacher.gender = gender
            teacher.DOB = date_of_birth
            teacher.phone_number = mobile
            teacher.Joine_date = joine_date
            teacher.address = address
            teacher.city = city
            teacher.state = state
            teacher.zipe_code = zipe_code
            teacher.title = title
            teacher.country = country
            teacher.subject = subject
            teacher.save()
            messages.success(request, 'Teacher successfully updated.')
            return redirect('hod:view_teacher')
        teacher = Teacher.objects.get(id=id)
        context = {
            'teacher':teacher,
            'subject':subject
        }
        return render(request, 'Dashbord/Edit_teacher.html', context)
    return redirect('error')
@login_required()
def Delete_teacher(request, id):
    user = request.user
    if user.user_type == 'admin':
        teacher = User.objects.get(id=id)
        teacher.delete()
        messages.success(request, 'Teacher succeccfully deleted!')
        return redirect('hod:view_teacher')
    else:
        return redirect('error')

@login_required()
def Add_Adviser(request):
    user = request.user
    if user.user_type == 'admin':
        if request.method == 'POST':
            adviser_name = request.POST.get('adviser_name')
            adviser_pic = request.FILES.get('adviser_pic')
            adviser_email = request.POST.get('email')
            title = request.POST.get('title')
            about_adviser = request.POST.get('about_adviser')

            rendom_int = random.randint(0, 1000)
            randon_str = str(rendom_int)
            adviser_id     = 'ADV'+randon_str

            adviser = Adviser(
                adviser_name = adviser_name,
                adviser_pic = adviser_pic,
                adviser_email = adviser_email,
                about_adviser = about_adviser,
                adviser_id = adviser_id,
                title = title,
            )
            adviser.save()
            messages.success(request, 'Adviser succssfuly added!')
            return redirect('hod:add_adviser')
        
        return render(request, 'Dashbord/add_adviser.html')
    return redirect('error')
@login_required()
def View_adviser(request):
    user = request.user
    if user.user_type == 'admin':
        advisers = Adviser.objects.all()
        context = {
            'advisers':advisers
        }
        return render(request, 'Dashbord/view_adviser.html', context)
    return redirect('error')
@login_required()
def Edit_adviser(request, id):
    user = request.user
    if user.user_type == 'admin':
        if request.method == 'POST':
            adviser_name = request.POST.get('adviser_name')
            title = request.POST.get('title')
            adviser_pic = request.FILES.get('adviser_pic')
            adviser_email = request.POST.get('email')
            about_adviser = request.POST.get('about_adviser')

            adviser = Adviser.objects.get(id=id)
            adviser.adviser_name = adviser_name
            adviser.title = title
            adviser.adviser_email = adviser_email
            adviser.about_adviser = about_adviser
            
            if adviser_pic !=None and adviser_pic !='':
                adviser.adviser_pic = adviser_pic

            adviser.save()
            messages.success(request, 'Adviser sucessfully Updated')
            return redirect('hod:view_adviser')



            print(adviser_name)
        adviser = Adviser.objects.get(id=id)
        context = {
            'adviser':adviser
        }
        return render(request, 'Dashbord/edit_adviser.html', context)
    else:
        return redirect('error')

@login_required()
def Delete_adviser(request, id):
    user = request.user
    if user.user_type == 'admin':
        adviser = Adviser.objects.get(id=id)
        adviser.delete()
        messages.success(request, 'Adviser sucessfully deleted!')
        return redirect('hod:view_adviser')
    return redirect('error')
@login_required()
def Add_Subject(request):
    user = request.user
    if user.user_type == 'admin' or user.user_type == 'teacher':
        if request.method == 'POST':
            subject_name = request.POST.get('subject_name')
            if subject_name == '':
                messages.warning(request, 'Enter subject name!')
                return redirect('hod:add_subject')
            subject = Subject(
                subject_name = subject_name,
            )
            subject.save()
            messages.success(request, 'Subject Successfully added!')
            return redirect('hod:add_subject')
        context = {

        }
        return render(request, 'Dashbord/add_subject.html', context)
    return redirect('error')
@login_required()
def View_subject(request):
    user = request.user
    if user.user_type == 'admin' or user.user_type == 'teacher':
        subjects = Subject.objects.all()
        context = {
            'subjects':subjects
        }
        return render(request, 'Dashbord/view_subject.html', context)
    return redirect('error')

@login_required()
def Edit_subject(request, id):
    user = request.user
    if user.user_type == 'admin' or user.user_type == 'teacher':
        if request.method == 'POST':
            subject_name = request.POST.get('subject_name')

            if subject_name == '':
                messages.warning(request, 'Enter subject name!')
                return redirect('hod:view_subject')
            
            subject = Subject.objects.get(id=id)
            subject.subject_name = subject_name
            subject.save()
            messages.success(request, 'Subject Successfully Updated!')
            return redirect('hod:view_subject')

        subject = Subject.objects.get(id=id)

        context = {
            'subject':subject
        }
        
        return render(request, 'Dashbord/edit_subject.html', context)
    return redirect('error')
@login_required()
def Delete_subject(request, id):
    user = request.user
    if user.user_type == 'admin' or user.user_type == 'teacher':
        subject = Subject.objects.get(id=id)
        subject.delete()
        messages.success(request, 'Subject Successfully Deleted!')
        return redirect('hod:view_subject')
    return redirect('error')
@login_required()
def Student_list(request):
    user = request.user
    if user.user_type == 'admin' or user.user_type == 'teacher':
        student = User.objects.filter(user_type='student')
        return render(request, 'Dashbord/student_list.html', context={'student':student})
    return redirect('error')

@login_required()
def HOD_profile(request):
    user = request.user
    if user.user_type == 'admin':
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            profile_pic = request.FILES.get('profile_pic')
            password = request.POST.get('password')
            user = User.objects.get(id=request.user.id)

            if profile_pic != None and profile_pic !='':
                user.profile_pic = profile_pic

            if password != '' and password != None:
                user.set_password(password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, 'Admin information successfully updated!')
            if password:
                return redirect('index')
            return redirect('hod:hod_profile')
        
        return render(request, 'Dashbord/hod_profile.html')
    return redirect('error')


@login_required()
def Add_book(request):
    user_type = request.user
    print(user_type)
    if user_type.user_type == 'admin' or user_type.user_type == 'teacher':
        if request.method == 'POST':
            book_name = request.POST.get('book_name')
            regular_price = request.POST.get('regular_price')
            discount_price = request.POST.get('discount_price')
            writer_name = request.POST.get('writer_name')
            pic = request.FILES.get('pic')
            description = request.POST.get('description')

            book = Books(
                name = book_name,
                writer_name = writer_name,
                description = description,
                picture = pic,
                regular_price = regular_price,
                discount_price = discount_price,
            )
            if user_type.user_type == 'admin':
                book.is_published = True
            book.save()
            messages.success(request, 'Book Successfully added')
            return redirect('hod:add_book')
        return render(request, 'Dashbord/Add_book.html')
    else:
        return redirect('error')
@login_required()
def View_book(request):
    user = request.user
    if user.user_type == 'admin' or user.user_type == 'teacher':
        book_list = Books.objects.all()
        context = {
            'book_list':book_list,
        }
        return render(request, 'Dashbord/view_book.html', context)
    return redirect('error')
@login_required()
def Update_book(request,id):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        if request.method == 'POST':
                book_name = request.POST.get('book_name')
                writer_name = request.POST.get('writer_name')
                regular_price = request.POST.get('regular_price')
                discount_price = request.POST.get('discount_price')
                pic = request.FILES.get('pic')
                description = request.POST.get('description')
                
                books = Books.objects.get(id=id)
                books.name = book_name
                books.writer_name = writer_name
                books.description = description
                books.regular_price = regular_price
                books.discount_price = discount_price
                if pic != None:
                    books.picture = pic

                books.save()
                messages.success(request, 'Book Successfully updated!')
                return redirect('hod:view_book')
        books = Books.objects.get(id=id)
        context = {
            'books':books
        }
        return render(request, 'Dashbord/update_book.html', context)
    else:
        return redirect('error')

@login_required()  
def Book_delete(request, id):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        book = Books.objects.get(id=id)
        book.delete()
        messages.success(request, 'Book successfully deleted!')
        return redirect('hod:view_book')
    else:
        return redirect('error')
    

@login_required()
def Approve_book(request, id):
    user_= request.user.user_type
    if user_ == 'admin':
        book= Books.objects.get(id=id)
        book.is_published = True
        book.save()
        messages.success(request, 'Book Published')
        return redirect('hod:view_book')
    else:
        return redirect('error')
@login_required()
def View_ContactUs(request):
    messeges = Contact_Us.objects.all()
    print(messeges)
    context = {
        'messeges':messeges
    }
    return render(request, 'Dashbord/view_contactus.html', context)
@login_required()   
def See_messege(request, id):
    contact = Contact_Us.objects.get(id=id)
    if contact:
        contact.is_read = True
        contact.save()
    context = {
        'contact':contact
    }
    return render(request, 'Dashbord/see_msg.html', context)
@login_required()
def Delete_msg(request, id):
    contact = Contact_Us.objects.get(id=id)
    contact.delete()
    return redirect('hod:view_contactus')

@login_required()
def Book_order_list(request):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        order_list = UserBook.objects.all()
        return render(request, 'Dashbord/order_list.html', context={'order_list':order_list})
    else:
        return redirect('error')
@login_required() 
def Deliver_book(request, id):
    user_= request.user.user_type
    if user_ == 'admin' or user_ == 'teacher':
        order = UserBook.objects.get(id=id)
        if order:
            order.delivery_status = True
            order.save()
            return redirect('hod:order_list')
        else:
            messages.error(request, 'Something Wrong!Pleae Try Again')
            return redirect('hod:order_list')
    else:
        return redirect('error')
