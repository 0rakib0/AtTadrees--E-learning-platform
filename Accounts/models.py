from django.db import models
from django.contrib.auth.hashers import make_password

# >>>>>>>>>>>>>>>>> for cerate superuser by email<<<<<<<<<<<<<<<<<
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy
from django.dispatch import receiver
from django.db.models.signals import post_save
from .manager import MyUserManager
# Create your models here.



class User(AbstractBaseUser, PermissionsMixin):
    email         = models.EmailField(unique=True, null=False)
    password      = models.CharField(max_length=120)
    first_name    = models.CharField(max_length=165, null=True, blank=True)
    last_name      = models.CharField(max_length=165, null=True, blank=True)
    profile_pic   = models.ImageField(upload_to='profile_pic', null=True, blank=True)

    user_rol = (
        ('admin','Admin'),
        ('teacher','Teacher'),
        ('student','Student'),
    )
    user_type = models.CharField(
        max_length=20, 
        choices=user_rol,
        )
    is_staff = models.BooleanField(
        gettext_lazy("staff status"),
        default=False,
        help_text = gettext_lazy("Designet whether this user can Login this site")
    )
    is_active = models.BooleanField(
        gettext_lazy("Active"),
        default=True,
        help_text = gettext_lazy("designates Whether this user should be creates as active. unselect this instad of deleting accounts")
    )
    
    # def save(self, *args, **kwargs):
    #     # Hash the password before saving the object
    #         self.password = make_password(self.password)
    #         super().save(*args, **kwargs)
    
    
    
    USERNAME_FIELD = 'email'
    objects = MyUserManager()
    
    def __str__(self) -> str:
        return self.email
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
    