from django.db import models
from django.conf import settings
from hitcount.models import HitCount, HitCountMixin
# Create your models here.

class DjangoBoard(models.Model,HitCountMixin):
      subject = models.CharField(max_length=50, blank=True)
      name = models.CharField(max_length=50, blank=True)
      nick_name = models.CharField(max_length=50, blank=True)
      created_date = models.DateField(null=True, blank=True)
      memo = models.CharField(max_length=200, blank=True)
      hits = models.IntegerField(default=0)

      def __str__(self):
          return self.subject
      
      @property
      def hit_update_counter(self):
          self.hits = self.hits + 1
          self.save()

class SubBoard(models.Model):
    subname = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.subname

class DataroomBoard(models.Model):
    sub = models.CharField(max_length=50, blank=True)
    item = models.CharField(max_length=10)
    name = models.CharField(max_length=50, blank=True)
    year = models.DateField()

class DataRoom(models.Model):
    sub = models.CharField(max_length=50, blank=True)
    item = models.CharField(max_length=10)
    title = models.CharField(max_length=50, blank=True)
    year = models.DateField()
    name = models.CharField(max_length=50, blank=True)