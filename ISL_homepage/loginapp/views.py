from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
#유저에 대한 클래스를 가져옴
from django.contrib import auth
#계정에 대한 권한

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        #request 방식이 POST이면
        if request.POST['password1'] == request.POST['password2']:
            #passwor1 과 password2값이 같으면
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            #사용자가 입력한 usernaeme과 password로 계정을 생성하여 user라는 변수에 담는다.
            auth.login(request, user)
            #로그인!
            return redirect('home')
            #redirect안에는 url을 담는다.
    return render(request,'sign_up.html')
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