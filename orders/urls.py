from django.urls import path
from .views import (
    AddToCartView, CreateOrderView, CartListView, OrderListView,
    OrderDetailByPKView, OrderDetailByUUIDView, RemoveFromCartView
)

urlpatterns = [
    path('cart/', CartListView.as_view(), name='cart'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/<int:pk>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('create/', CreateOrderView.as_view(), name='create-order'),
    path('', OrderListView.as_view(), name='orders'),
    path('<int:pk>/', OrderDetailByPKView.as_view(), name='order-detail-pk'),
    path('uuid/<uuid:order_id>/', OrderDetailByUUIDView.as_view(), name='order-detail-uuid'),
]