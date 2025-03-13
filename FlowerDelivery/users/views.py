from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from orders.models import Order  # Импортируем модель заказов


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


@login_required
def profile_view(request):
    user = request.user  # Получаем текущего пользователя

    # Получаем все заказы пользователя, сортируем по дате (новые сверху)
    orders = Order.objects.filter(user=user).order_by('-created_at')

    if request.method == "POST":
        # Обновляем поля пользователя, если они переданы
        if "phone" in request.POST:
            user.phone_number = request.POST["phone"]
        if "birth_date" in request.POST:
            user.birth_date = request.POST["birth_date"]
        if "address" in request.POST:
            user.address = request.POST["address"]
        if "avatar" in request.FILES:
            user.avatar = request.FILES["avatar"]

        user.save()
        return JsonResponse({"status": "success"})

    # Передаём заказы в шаблон
    return render(request, "users/profile.html", {"orders": orders})