from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('total_price', 'ordered_at', 'user', 'cart')

    fields = ('name', 'email', 'address', 'total_price', 'ordered_at', 'user', 'cart', 'status')
