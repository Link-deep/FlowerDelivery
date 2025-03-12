from django.shortcuts import render, redirect
from .models import GamesPost
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import GameForm



def index(request):
    games_list = GamesPost.objects.only("title", "image", "price", "discount_percent")  # Выбираем только нужные поля

    # Добавляем пагинацию (по 12 товаров на страницу)
    paginator = Paginator(games_list, 12)
    page_number = request.GET.get('page')  # Получаем номер страницы из запроса
    games = paginator.get_page(page_number)

    return render(request, 'catalog/catalog.html', {'games': games})


def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(is_admin)
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = GameForm()

    return render(request, 'catalog/add_game.html', {'form': form})