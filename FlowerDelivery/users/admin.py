from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительная информация", {"fields": ("phone_number", "avatar", "birth_date", "address")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Дополнительная информация", {"fields": ("phone_number", "avatar", "birth_date", "address")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
