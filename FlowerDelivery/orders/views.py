from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from catalog.models import GamesPost
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


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



@login_required
@staff_member_required  # Только для администраторов
def list_orders(request):
    orders = Order.objects.all().order_by('-created_at')  # Получаем все заказы (без фильтрации)
    return render(request, "orders/list_orders.html", {"orders": orders})


@csrf_exempt  # Разрешает запросы без CSRF-токена (AJAX использует его в headers)
@staff_member_required  # Только для администраторов
def update_order_status(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Получаем JSON-данные
            order_id = data.get("order_id")
            new_status = data.get("status")

            # Ищем заказ по ID
            order = Order.objects.get(id=order_id)
            order.status = new_status
            order.save()

            return JsonResponse({"status": "success"})
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Заказ не найден!"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "error", "message": "Неверный запрос"})