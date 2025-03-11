from django.db import models
from decimal import Decimal


class GamesPost(models.Model):
	title = models.CharField('Название Игры', max_length=100)
	description = models.TextField('Описание', max_length=500)
	image = models.ImageField('Изображение', upload_to='media/games/')

	price = models.DecimalField('Цена', max_digits=10, decimal_places=2)  # Цена
	discount_percent = models.PositiveIntegerField('Скидка (%)', default=0)  # Процент скидки

	stock = models.PositiveIntegerField('Количество на складе', default=0)  # Остаток на складе
	release_date = models.DateField('Дата выхода', null=True, blank=True)  # Дата релиза
	platform = models.CharField('Платформа', max_length=50, choices=[  # Платформа игры
		('Switch', 'Nintendo Switch'),
		('PS5', 'PlayStation 5'),
		('Xbox', 'Xbox Series X')
	], default='Switch')

	publisher = models.CharField('Издатель', max_length=100, blank=True, null=True)  # Издатель игры
	genre = models.CharField('Жанр', max_length=100, blank=True, null=True)  # Жанр игры

	created_at = models.DateTimeField('Дата добавления', auto_now_add=True)  # Когда добавили в базу
	updated_at = models.DateTimeField('Дата обновления', auto_now=True)  # Когда обновили запись



	def get_discounted_price(self):
		"""Возвращает цену с учетом скидки"""
		discount = Decimal(self.discount_percent) / Decimal(100)  # Преобразуем процент в Decimal
		return round(self.price * (Decimal(1) - discount), 2)

	def __str__(self):
		return f"{self.title} - ({self.platform}) - {self.price} руб."

	class Meta:
		verbose_name = "Игровой картридж"
		verbose_name_plural = "Игровые картриджи"
		ordering = ['-created_at']  # Сортировка по дате добавления
