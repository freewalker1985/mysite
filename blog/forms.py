from .models import UserInfo
from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField


class UserInfoForm(forms.Form):
    gender = (('male', '男'), ('female', '女'))
    username = forms.CharField(label='用户名', max_length=20,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    nickname = forms.CharField(label='昵称', max_length=20,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password = forms.CharField(label='密码', max_length=8)
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='确认密码', max_length=8,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='邮箱')
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20,widget=forms.TextInput(attrs={'class': 'form-control' ,'placeholder': "Username",'autofocus': ''}))
    password = forms.CharField(label='密码', max_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))
    captcha = CaptchaField(label='验证码')
