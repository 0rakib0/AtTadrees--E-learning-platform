from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserRegister, name='register'),
    path('login/', views.UserLogin, name='login'),
    path('user-logout/', views.User_logout, name='user_logout')
]
