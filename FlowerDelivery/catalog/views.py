from django.shortcuts import render
from .models import GamesPost
from django.core.paginator import Paginator



def index(request):
    games_list = GamesPost.objects.only("title", "image", "price", "discount_percent")  # Выбираем только нужные поля

    # Добавляем пагинацию (по 12 товаров на страницу)
    paginator = Paginator(games_list, 12)
    page_number = request.GET.get('page')  # Получаем номер страницы из запроса
    games = paginator.get_page(page_number)

    return render(request, 'catalog/catalog.html', {'games': games})