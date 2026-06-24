from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'category',
        'stock',
        'rating'
    )

    search_fields = (
        'name',
        'brand',
        'category'
    )