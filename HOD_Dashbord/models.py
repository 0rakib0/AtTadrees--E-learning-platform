from django.db import models
from Accounts.models import User
import uuid
# Create your models here.


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    DOB = models.CharField(max_length=20, blank=True, null=True)
    Joine_date = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=120, blank=True, null=True)
    address = models.CharField(max_length=260, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    zipe_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    
    def __str__(self) -> str:
        return str(self.user.email)
    
class Adviser(models.Model):
    adviser_id = models.CharField(max_length=20)
    adviser_name = models.CharField(max_length=120)
    title = models.CharField(max_length=100, null=True, blank=True)
    adviser_pic = models.ImageField(upload_to='adviser')
    adviser_email = models.EmailField()
    about_adviser = models.TextField()
    
    
    def __str__(self) -> str:
        return str(self.adviser_name)

class Subject(models.Model):
    subject_name = models.CharField(max_length=120)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.subject_name    

