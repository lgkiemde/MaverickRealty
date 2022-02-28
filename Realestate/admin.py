from django.contrib import admin

from .models import Customer, Property, LienParcels


class CustomerList(admin.ModelAdmin):
    list_display = ('cust_fname', 'cust_lname', 'buying_time', 'price_range_min', 'price_range_max')
    list_filter = ('cust_lname', 'buying_time', 'price_range_min', 'price_range_max')
    search_fields = ('cust_lname', 'buying_time', 'price_range_min', 'price_range_max')
    ordering = ['cust_lname', 'buying_time', 'price_range_min', 'price_range_max']


class PropertyList(admin.ModelAdmin):
    list_display = ('address', 'city', 'state', 'bedrooms', 'bathrooms')
    list_filter = ('address', 'city', 'state', 'bedrooms', 'bathrooms')
    search_fields = ('address', 'city', 'state', 'bedrooms', 'bathrooms')
    ordering = ['address', 'city', 'state', 'bedrooms', 'bathrooms']


class LiensList(admin.ModelAdmin):
    list_display = ('address', 'city', 'state', 'zip', 'tax_link')
    list_filter = ('address', 'city', 'state', 'zip', 'tax_link')
    search_fields = ('address', 'city', 'state', 'zip', 'tax_link')
    ordering = ['address', 'tax_link']


admin.site.register(Customer)
admin.site.register(Property, PropertyList)
admin.site.register(LienParcels, LiensList)
