from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),

   
]