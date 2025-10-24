from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    size = filters.CharFilter(field_name='sizes__size', lookup_expr='iexact')
    color = filters.CharFilter(field_name='colors__color_name', lookup_expr='iexact')
    tag = filters.CharFilter(field_name='tags__tag__name', lookup_expr='iexact')
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['category', 'brand', 'size', 'color', 'tag', 'min_price', 'max_price']