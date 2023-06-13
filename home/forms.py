from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Article
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        
# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ['title','content','image','author','published_date']

class LoginForm(AuthenticationForm):
    pass

