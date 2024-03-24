from django.contrib import admin
from .models import Books, Category, Course, Lesson, Video, Languege, Whats_learn, Requierment, UserCourse, Contact_Us, Payment, UserBook
# Register your models here.

admin.site.register(Books)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(Languege)
admin.site.register(Whats_learn)
admin.site.register(Requierment)
admin.site.register(UserCourse)
admin.site.register(Contact_Us)
admin.site.register(Payment)
admin.site.register(UserBook)