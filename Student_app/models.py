from django.db import models
from clac.models import Course
from Accounts.models import User
# Create your models here.



class Course_Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='crs_review')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=260)
    review_massage = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.user.first_name) + '-' + str(self.course.title_1)
    
class Student_Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_massage = models.TextField()

    def __str__(self) -> str:
        return str(self.user.first_name) + '-' + str(self.course.title_1)




