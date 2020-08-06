from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
#유저에 대한 클래스를 가져옴
from django.contrib import auth
#계정에 대한 권한
from .models import Profile
from .forms import SignupForm, ProfileForm
from django.db import transaction

# Create your views here.

@transaction.atomic
def sign_up(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if signup_form.is_valid() and profile_form.is_valid():
            signup_form.signup()
            profile_form.profile_save(User.objects.get(username=signup_form.cleaned_data['username']))
            return redirect('home')
        else:
            print('error' + str(signup_form.is_valid()) + str(profile_form.is_valid()))
    else:
        signup_form=SignupForm()
        profile_form = ProfileForm()
    
    return render(request,'sign_up.html', {'signup_form':signup_form, 'profile_form':profile_form})
    # 실패하는경우 sign_up.html에 머문다.

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        # 사용자가 입력한 ID를 username에 담는다.
        password = request.POST['password']
        # 사용자가 입력한 password를 passwor에 담는다.
        user = auth.authenticate(request, username=username, password=password)
        # 데이터베이스에 입력한 username과 password가 있는지 확인한다.
        if user is not None:
            auth.login(request, user)
            #ID와 password가 존재하면 로그인
            # messages.info(request,'로그인 되었습니다.')
            # 로그인 성공시 성공 알림 띄우기
            return redirect("home")
        else:
            return render(request, 'sign_in.html', {'error': 'ID or password is incorrect.'})
    else:
        return render(request, 'sign_in.html')
    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request,"sign_in.html")