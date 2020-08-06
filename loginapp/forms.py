from django import forms
from django.contrib.auth import get_user_model
from .models import Profile
User = get_user_model()

class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':"ID"
                
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder':"비밀번호"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder':"비밀번호 확인"
            }
        )
    )
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('아이디가 이미 사용중입니다.')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        return password2

    def signup(self):
        if self.is_valid():
            return User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password2'],
            )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'student_ID', 'email')
        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : '이름',
            }),
            'student_ID' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : '학번',
            }),
            'email' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'email',
            }),
        }
    def profile_save(self, username):
         if self.is_valid():
           return Profile.objects.create(
               user=username, 
               email = self.cleaned_data['email'],
               name = self.cleaned_data['name'],
               student_ID= self.cleaned_data['student_ID']
               )
