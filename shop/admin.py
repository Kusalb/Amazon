from django.contrib import admin

# Register your models here.
from shop.models import *
from django.contrib.auth.models import Group


admin.site.unregister(Group)

admin.site.site_header = "Naya heading"

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'venue', 'manager', 'description')
    list_editable = ('venue', 'manager')
    search_fields = ('name', 'date', 'venue', 'manager', 'description')

class ShopAdmin(admin.ModelAdmin):
    list_display = ('shop_name', 'contact', 'location', 'contact_person', 'email')
    search_fields = ('shop_name', 'contact', 'location', 'contact_person', 'email')
    list_editable = ['contact', 'contact_person', 'email']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'discount', 'old_price')
    search_fields = ('product_name', 'price', 'discount', 'old_price')
    list_editable = ['price', 'discount']

class DealAdmin(admin.ModelAdmin):
    list_display = ('deal_name', 'valid_from', 'valid_till', 'discount_percentage')
    search_fields = ('deal_name', 'valid_from', 'valid_till', 'discount_percentage')
    list_editable = ['valid_from', 'valid_till', 'discount_percentage']


admin.site.register(Event, EventAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Deal, DealAdmin)

