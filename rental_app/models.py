from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.exceptions import ValidationError

def __str__(self):
        return str(self.type_name)

class BedType(models.Model):
    type_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.type_name

class Customer (models.Model):
        first_name = models.CharField(max_length=100, blank=True, null=True)
        last_name = models.CharField(max_length=100, blank=True, null=True)
        dob = models.DateField()
        gender = models.CharField(max_length=8)
        email = models.CharField(max_length=100,unique=True)
        address1 = models.CharField(max_length=250)
        address2 = models.CharField(max_length=250)
        mobile = models.CharField(max_length=14, unique=True)


        def __str__(self):
            full_name = self.first_name+' '+self.last_name
            return full_name

class Book (models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    check_in = models.DateField()
    check_out = models.DateField()
    room_number = models.PositiveIntegerField()
    BedType = models.ForeignKey(BedType, on_delete=models.CASCADE)
    special_req = models.CharField(max_length=250)

    def __str__(self):
        return self.customer_id.first_name

    def clean(self):
        super(Book, self).clean()
        req_Book = Book.objects.filter(room_number=self.room_number)

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
