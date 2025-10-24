from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.http import HttpRequest
from django.db.models import QuerySet
from .models import Order, OrderItem, CartItem

# 🧾 Custom Actions for Orders
def mark_as_completed(modeladmin: ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(status='Completed')
mark_as_completed.short_description = "Mark selected orders as Completed"

def mark_as_cancelled(modeladmin: ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(status='Cancelled')
mark_as_cancelled.short_description = "Mark selected orders as Cancelled"

# 📦 Inline Order Items inside Order
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price', 'product_name', 'product_price_at_order')
    can_delete = False
    show_change_link = False

# 🧾 Order Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'status', 'total', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order_id', 'user__username')
    readonly_fields = ('order_id', 'user', 'total', 'created_at', 'updated_at')
    inlines = [OrderItemInline]
    actions = [mark_as_completed, mark_as_cancelled]

# 🛒 Cart Admin
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'added_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('added_at',)
    list_editable = ('quantity',)

# 📦 Optional: Register OrderItem directly
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_name', 'quantity', 'price')
    search_fields = ('order__order_id', 'product_name')
    readonly_fields = ('order', 'product', 'product_name', 'product_price_at_order', 'price')
    list_filter = ('product_name',)