from django.db import models
from django.conf import settings
from django.utils import timezone
from hitcount.models import HitCount, HitCountMixin
from django.contrib.auth.models import User
# Create your models here.

class DjangoBoard(models.Model,HitCountMixin):
      subject = models.CharField(max_length=50, null=True)
      content = models.CharField(max_length=50, null=True)
      author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
      created_date = models.DateField('date_published')
      hits = models.IntegerField(default=0)
      file = models.FileField(upload_to="%Y/%m/%d", null=True, blank=True)

      
      def __str__(self):
          return self.subject
      
      @property
      def hit_update_counter(self):
          self.hits = self.hits + 1
          self.save()
