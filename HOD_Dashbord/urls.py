from django.urls import path
from . import views

app_name = 'hod'

urlpatterns = [
    # --------------------> HOD urls path <---------------------
    path('hod-dashbord/', views.Dashbord, name='hod_dashbord'),
    path('admin-profile/', views.HOD_profile, name='hod_profile'),


    # --------------------> Teachers urls path <---------------------
    path('Add-teacher/', views.Add_teacher, name='add_teacher'),
    path('view-teacher/', views.View_Teacher, name='view_teacher'),
    path('Edit-teacher/<int:id>/', views.Edit_Teacher, name='edit_teacher'),
    path('delete-teaher/<int:id>/', views.Delete_teacher, name='delete_teacher'),

    # --------------------> Adviser urls path <---------------------
    path('add-adviser/', views.Add_Adviser, name='add_adviser'),
    path('view-adviser/', views.View_adviser, name='view_adviser'),
    path('edit-adviser/<int:id>/', views.Edit_adviser, name='edit_adviser'),
    path('delete-adviser/<int:id>/', views.Delete_adviser, name='delete_adviser'),


    # --------------------> Subjest urls path <---------------------
    path('add-subject/', views.Add_Subject, name='add_subject'),
    path('view-subject/', views.View_subject, name='view_subject'),
    path('edit-subject/<int:id>/', views.Edit_subject, name='edit_subject'),
    path('delete-subject/<int:id>/', views.Delete_subject, name='delete_subject'),


    # --------------------> Student urls path <---------------------
    path('student-list/', views.Student_list, name='student_list'),

    # --------------------> Book urls path <---------------------

    path('add-book/', views.Add_book, name='add_book'),
    path('view-book/', views.View_book, name='view_book'),
    path('update-book/<int:id>/', views.Update_book, name='update_book'),
    path('delete-book/<int:id>/', views.Book_delete, name='delete_book'),
    path('book-approve/<int:id>/', views.Approve_book, name='approve_book'),


    # ============================> View Student messge / Contact Us form ======================>
    
    path('view-contct-us/', views.View_ContactUs, name='view_contactus'),
    path('see-messge/<int:id>/', views.See_messege, name='see_msg'),
    path('delete-messge/<int:id>/', views.Delete_msg, name='delete_msg'),


    path('book-order-list/', views.Book_order_list, name='order_list'),
    path('deliverd_book/<int:id>/', views.Deliver_book, name='delivered_book'),
]
