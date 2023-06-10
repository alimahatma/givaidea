from django.shortcuts import render, redirect
from .forms import RegisterForm


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
            return redirect('home')
    else:
            form = RegisterForm()
            context = {'form':form}
    return render(request, 'home/register.html', context)


