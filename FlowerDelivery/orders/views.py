from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from catalog.models import GamesPost
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

@login_required
def create_order(request, game_id):

    game = get_object_or_404(GamesPost, id=game_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.game = game

            # Заполняем отсутствующие данные
            order.full_name = form.cleaned_data.get('full_name', request.user.username)  # ФИО из формы или имя пользователя
            order.phone = form.cleaned_data.get('phone', request.user.phone_number)  # Телефон из формы или профиля
            order.quantity = form.cleaned_data.get('quantity', 1)  # Количество (по умолчанию 1)
            order.total_price = game.get_discounted_price() * order.quantity  # Считаем сумму заказа
            order.save()
            return redirect('order_success')
        else:
            print("Форма не валидна. Ошибки:", form.errors)  # Выведет ошибки в консоль
    else:
        form = OrderForm()

    return render(request, 'orders/create_order.html', {'form': form, 'game': game})



def order_success(request):
    return render(request, 'orders/order_success.html')
