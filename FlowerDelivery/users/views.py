from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, UserLoginForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('profile')  # Перенаправление в личный кабинет
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def profile_view(request):
    return render(request, 'users/profile.html')
