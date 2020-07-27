from django.db import models
from django.conf import settings
from django.utils import timezone
from hitcount.models import HitCount, HitCountMixin
# Create your models here.

class DjangoBoard(models.Model,HitCountMixin):
      subject = models.CharField(max_length=50, blank=True)
      name = models.CharField(max_length=50, blank=True)
      nick_name = models.CharField(max_length=50, blank=True)
      created_date = models.DateField(null=True, blank=True)
      memo = models.CharField(max_length=200, blank=True)
      hits = models.IntegerField(default=0)
      photo = models.ImageField(upload_to='images/', null=True)

      
      def __str__(self):
          return self.subject
      
      @property
      def hit_update_counter(self):
          self.hits = self.hits + 1
          self.save()
