from django.contrib import admin
from django.urls import path, include
from mainapp.views import home
from django.conf.urls.static import static
from django.conf import settings
import mainapp.views
import boardapp.views
import loginapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainapp.views.home, name="home"),
    path('index',mainapp.views.index, name="index"),
    path('board/',boardapp.views.board, name="board"),
    path('write', boardapp.views.write, name="write"),
    path('create', boardapp.views.create, name="create"),
    path('board/<int:board_id>/',boardapp.views.detail,name="detail"),
    path('update/<int:board_id>/',boardapp.views.update,name="update"),
    path('delete/<int:board_id>/',boardapp.views.delete,name="delete"),
    path('sign_up',loginapp.views.sign_up,name="sign_up"),
    path('sign_in',loginapp.views.sign_in,name="sign_in"),
    path('logout',loginapp.views.logout, name="logout"),
    path('dataroom/', boardapp.views.dataroom, name="dataroom"),
    path('accounts/',include('allauth.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
