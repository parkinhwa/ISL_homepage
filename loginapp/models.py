from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='이메일', blank=True)
    name = models.CharField(max_length=10,verbose_name='이름', blank=True)
    student_ID = models.IntegerField(verbose_name='학번', blank=True, null=True)
    
