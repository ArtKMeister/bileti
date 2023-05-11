from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLogin, UserRegistration, UserProfile
from django.contrib import auth
from users.models import User

# Create your views here.

def authorization(request):
    if request.method == 'POST':
        form = UserLogin(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLogin()
    context = {'form': form}
    return render(request, 'users/auth.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistration(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:authorization'))
    else:
        form = UserRegistration()
    context = {'form': form}
    return render(request, 'users/reg.html', context)

def profile(request):
    if request.method == 'POST':
        form = UserProfile(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfile(instance=request.user)
    context = {
        'form': form,
        'login': User.objects.all()
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))