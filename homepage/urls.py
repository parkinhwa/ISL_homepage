"""homepage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import mainapp.views
import boardapp.views
import loginapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainapp.views.home, name="home"),
    path('board/',boardapp.views.board, name="board"),
    path('write', boardapp.views.write, name="write"),
    path('create', boardapp.views.create, name="create"),
    path('board/<int:board_id>/',boardapp.views.detail,name="detail"),
    path('sign_up',loginapp.views.sign_up,name="sign_up"),
    path('sign_in',loginapp.views.sign_in,name="sign_in"),
    path('accounts/',include('allauth.urls')),
]
