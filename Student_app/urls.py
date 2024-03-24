from django.urls import path
from . import views
app_name = 'student'


urlpatterns = [
    path('student-dashbord/', views.Student_dashbord, name='student_dashbord'),
    path('student-profile/', views.Student_profile, name='student_profile'),
    path('my-course/', views.MyCourse, name='my_course'),
    path('student-rating/', views.Student_Ratings, name='student_ratings'),
    path('view-video-plylist/<slug:slug>/', views.Video_Video_playlist, name='video_plylist'),
    path('my-books/', views.My_book, name='my_book'),
]
