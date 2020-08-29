from django.contrib import admin
from .models import DjangoBoard
from .models import SubBoard
from .models import DataRoom
# Register your models here.

admin.site.register(DjangoBoard)
admin.site.register(SubBoard)
admin.site.register(DataRoom)
