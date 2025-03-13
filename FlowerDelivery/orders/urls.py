from django.urls import path
from .views import create_order, order_success, list_orders, update_order_status

urlpatterns = [
    path('buy/<int:game_id>/', create_order, name='create_order'),
    path('success/', order_success, name='order_success'),
    path('list/', list_orders, name='list_orders'),
    path('update-order-status/', update_order_status, name='update_order_status'),
]

