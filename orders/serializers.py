from rest_framework import serializers
from .models import Order, OrderItem, CartItem
from products.serializers import ProductSerializer
from products.models import Product

# 🛒 Cart Item Serializer
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = CartItem
        fields = [
            'id', 'user', 'product', 'product_id', 'quantity', 'added_at'
        ]
        read_only_fields = ['id', 'user', 'product', 'added_at']

    def create(self, validated_data):
        user = self.context['request'].user
        product = validated_data['product']
        quantity = validated_data.get('quantity', 1)

        # ✅ If item already in cart → update quantity
        cart_item, created = CartItem.objects.get_or_create(
            user=user, product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return cart_item


# 📦 Order Item Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            'id', 'order', 'product', 'quantity', 'price',
            'product_name', 'product_price_at_order'
        ]
        read_only_fields = ['id', 'order', 'product_name', 'product_price_at_order']


# 🧾 Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'order_id', 'user', 'status', 'total',
            'created_at', 'updated_at', 'items'
        ]
        read_only_fields = [
            'id', 'order_id', 'user', 'total',
            'created_at', 'updated_at', 'items'
        ]

    def create(self, validated_data):
        """Create order automatically from user's cart"""
        user = self.context['request'].user
        order = Order.objects.create(user=user)

        cart_items = CartItem.objects.filter(user=user)
        if not cart_items.exists():
            raise serializers.ValidationError("Your cart is empty!")

        # ✅ Move items from Cart → OrderItem
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price,
                product_name=cart_item.product.name,
                product_price_at_order=cart_item.product.price
            )

        # ✅ Empty the cart after successful order
        cart_items.delete()

        # ✅ Recalculate total and save order
        order.save()
        return order