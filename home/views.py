from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    return render(request, 'home/home.html')


def skill_track(request):
    return render(request, 'home/skill_track.html')

def affiliate(request):
    return render(request, 'home/affiliate.html')


def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            messages.success(request, 'Registration successfull. You can now login.')
            return redirect('register')
    else:
            form = RegisterForm()
            context = {'form':form}
    return render(request, 'home/register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('superadmin')
            else :
                return redirect('home') 
    else:
        form = LoginForm()
    
    context = {
        'form': form
    }
    return render(request, 'home/login.html', context)






