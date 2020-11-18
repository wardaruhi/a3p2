
from django.contrib import admin
from rental_app.models import BedType, Book, Customer
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    model = Customer

admin.site.register(Book)
admin.site.register(BedType)
