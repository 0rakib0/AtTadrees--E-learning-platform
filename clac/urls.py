
from django. urls import path
from . import views



urlpatterns = [
   path('', views.homepage, name='index'),
   path('course-list/', views.Course_list, name='course_list'),
   path('books/', views.Book, name='books'),
   path('view-single-book/<int:id>/', views.View_single_Book, name='single_book'),
   path('single-course/<slug>/', views.Single_course_page, name='single_course'),
   path('404-error/', views.Error, name='error'),
   # ======================> Category <============================
   path('add-category/', views.Add_category, name='add_category'),
   path('view-category/', views.View_category, name='view_category'),
   path('Update-category/<int:id>/', views.Updat_category, name='update_category'),
   path("cetegory-delete/<int:id>/", views.Delete_Category, name='delete_category'),

   # ======================> Language <============================
   path('add-language/', views.Add_Languege, name='add_language'),
   path('view-language/', views.View_language, name='view_language'),
   path('delete-language/<int:id>/', views.Delete_Language, name='delete_language'),

   # ======================> Course <============================
   path('add-course/', views.Add_Course, name='add_course'),
   path('view-course/', views.View_course, name='view_course'),
   path('update-course/<int:id>/', views.Update_course, name='update_course'),
   path('course-delete/<int:id>/', views.Delete_course, name='delete_course'),
   path('publish-course/<int:id>/', views.Purlish_course, name='publish_course'),

   # ======================> Whats Learn from This corse <============================

   path('whats-learn/', views.Whats_learn_from_course, name='whats_learn'),
   path('view-whats-learn-from-course', views.View_whats_learn, name='view_whats_learn'),
   path('update-whats-learn/<int:id>/', views.Update_whats_learn, name='updated_wahts_learn'),

   # ======================> Course Requirment <============================

   path('add-course-requirment/', views.Add_cours_requirment, name='add_course_requirment'),
   path('view-course-requirment/', views.View_course_requirment, name='view_course_requirment'),
   path('update-course-requirment/<int:id>/', views.Update_course_requirment, name='update_course_requierment'),

   #========================> Lessone <========================================

   path('add-lesson/', views.Add_lesson, name='add_lesson'),
   path('View-lesson/', views.View_leson, name='view_lesson'),
   path('update-lesson/<int:id>/', views.Update_Lesson, name='update_lesson'),
   path('delete-lesson/<int:id>/', views.Delete_lesson, name='delete_lesson'),

   #========================> Course Video <========================================
   path('add-video/', views.Add_Video, name='add_video'),
   path('view-video/', views.View_Video, name='view_video'),
   path('delete-video/<int:id>/', views.Delete_video, name='delete_video'),

   # ======================> Enroll Course <========================================
   path('checkout/<slug:slug>/', views.Checkout, name='checkout'),
   path('book-checkout/<int:id>/', views.Book_checkout, name='book_checkout'),

   # ======================> Course Review & Rating <==============================
   path('course-review/', views.Course_Reviews, name='course_review' ),



   # ======================> Contact Us <================================
   path('contact-us/', views.Contact_Use, name='contact_us'),

   # =====================> success & faild URL <================================
   path('payment/payment-success/', views.payment_success, name='payment_success'),
   path('payment/payment-faild/', views.payment_failure, name='payment_failure'),
]
