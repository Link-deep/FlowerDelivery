from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):  # Наследуем стандартного пользователя Django
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Телефон")
    avatar = models.ImageField(upload_to='media/avatars/', blank=True, null=True, verbose_name="Аватар")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    address = models.TextField(blank=True, null=True, verbose_name="Адрес доставки")

    # Указываем уникальные related_name, чтобы избежать конфликта с auth.User
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions_set",
        blank=True
    )

    def __str__(self):
        return self.username
