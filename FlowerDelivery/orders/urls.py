from django.urls import path
from .views import create_order, order_success

urlpatterns = [
    path('buy/<int:game_id>/', create_order, name='create_order'),
    path('success/', order_success, name='order_success'),
]

