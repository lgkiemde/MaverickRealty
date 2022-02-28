from django import forms
from .models import Customer, Property, LienParcels

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_fname', 'cust_lname', 'buying_time', 'price_range_max', 'price_range_min', 'address',
                      'city', 'state', 'zipcode', 'email','phone_number')


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('address', 'city', 'state', 'zip', 'price', 'bedrooms',
                      'bathrooms', 'squarefeet', 'garagespaces', 'school_districts')


class LiensForm(forms.ModelForm):
    class Meta:
        model = LienParcels
        fields = ('address', 'city', 'state', 'zip', 'owner', 'lot_number',
                      'block_number', 'acres', 'tax_link', 'landvaluation_link')
