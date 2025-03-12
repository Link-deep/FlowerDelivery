from django.db import models
from django.contrib.auth import get_user_model
from catalog.models import GamesPost



User = get_user_model()  # Используем кастомную модель пользователя

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('processing', 'Обработка'),
        ('shipped', 'Отправлено'),
        ('delivered', 'Доставлено'),
        ('cancelled', 'Отменено'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Покупатель")
    game = models.ForeignKey(GamesPost, on_delete=models.CASCADE, verbose_name="Игра")
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    address = models.TextField(verbose_name="Адрес доставки")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма заказа")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус заказа")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")

    def __str__(self):
        return f"Заказ #{self.id} - {self.user.username} - {self.game.title}"
