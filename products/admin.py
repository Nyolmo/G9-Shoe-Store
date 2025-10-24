from django.contrib import admin
from .models import Product, Category, ProductImage, SizeVariant, ColorVariant, Tag, ProductTag


# Inline images inside Product
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # how many empty image forms to show
    fields = ('image', 'alt_text')
    readonly_fields = ()  # you can leave this empty or include 'image_preview' if you add a preview later


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')

    inlines = [ProductImageInline]  # 👈 this enables adding images directly in the Product form


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Optional — register other models too so you can manage them in admin
admin.site.register(SizeVariant)
admin.site.register(ColorVariant)
admin.site.register(Tag)
admin.site.register(ProductTag)
