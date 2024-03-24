from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def UserRegister(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')
        re_password = request.POST.get('re_pass')

        print(email)
        print(password)
        

        if User.objects.filter(email=email).first():
            messages.warning(request, 'Email Already Exist!')
            return redirect('index')
        
        elif password != re_password:
            messages.warning(request, 'Password Not match..')
            return redirect('index')
        
        else:
            Student = User(
                email = email,
                user_type = 'student',
            )
            Student.set_password(password)
            Student.save()
            messages.success(request, 'Account successfully created! Please Login..')
            return redirect('index')
    return render(request, 'Accounts/register.html')


def UserLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')

        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            user = request.user
            print(request.user.user_type)
            if user.user_type == 'student':
                return redirect('student:student_dashbord')
            if user.user_type == 'teacher':
                return redirect('Teacher_ap:teacher_dashbord')

            if user.user_type == 'admin':
                return redirect('hod:hod_dashbord')
        
        else:
            messages.error(request, 'Email and password Not match!')
            return redirect('index')
    return redirect('index')

@login_required()
def User_logout(request):
    logout(request)
    return redirect('index')