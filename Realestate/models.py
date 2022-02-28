from django.utils import timezone
from django.db import models


# Create your models here.
class Customer(models.Model):
    cust_fname = models.CharField(max_length=50, blank=False)
    cust_lname = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=False)
    buying_time = models.DateField(blank=False)
    price_range_min = models.CharField(max_length=30, blank=False)
    price_range_max = models.CharField(max_length=30, blank=False)
    created_date = models.DateField(
        default=timezone.now)
    updated_date = models.DateField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_lname)


class Property(models.Model):
    details = models.CharField(max_length=1000, blank=True)
    address = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=50, blank=False)
    zip = models.CharField(max_length=10, blank=False)
    price = models.DecimalField(max_digits=20, blank=False, decimal_places=2)
    bedrooms = models.IntegerField(blank=False)
    bathrooms = models.DecimalField(max_digits=10, blank=False, decimal_places=1)
    squarefeet = models.IntegerField(blank=False)
    HeatType = models.CharField(max_length=20)
    ACType = models.CharField(max_length=20)
    garagespaces = models.IntegerField()
    school_districts = models.CharField(max_length=50)
    created_date = models.DateField(default=timezone.now)
    updated_date = models.DateField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.address)


class LienParcels(models.Model):
    owner = models.CharField(max_length=50, blank=False)
    address = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='lien')
    city = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=50, blank=False)
    zip = models.CharField(max_length=10, blank=False)
    lot_number = models.CharField(max_length=20, blank=False)
    block_number = models.CharField(max_length=20, blank=False)
    acres = models.DecimalField(max_digits=20, decimal_places=2)
    tax_link = models.CharField(max_length=100, blank=False)
    landvaluation_link = models.CharField(max_length=100, blank=False)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.address)
