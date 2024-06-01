from django.contrib import admin
from main.models import Supplier, Network, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'country', 'city', 'street', 'building', 'debt']
    list_filter = ['city']
    search_fields = ['name']
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        """Очищаем задолженность"""
        queryset.update(arrears=0)
    clear_debt.short_description = "Очистить задолженность перед поставщиком"


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'city', 'street', 'building', 'supplier']
    list_filter = ['city']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'release_date', 'network', 'created_at']
