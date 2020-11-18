from django import forms
from django.forms import ValidationError
from django.core import validators
from django.contrib.auth.models import User
from rental_app.models import UserInfo, Book, Customer


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

#--------------------------------------------------------------------------------
class DateInput(forms.DateInput):
    input_type = 'date'


class FormBook(forms.ModelForm):

    class Meta():
        widgets = {'check_in' : DateInput(), 'check_out' : DateInput}
        model = Book
        fields = ('customer_id','check_in','check_out','BedType', 'special_req', 'room_number')

class FormCustomer(forms.ModelForm):

    class Meta():
        widgets = {'dob': DateInput()}
        model = Customer
        fields = ('first_name', 'last_name', 'dob', 'gender', 'email', 'address1', 'address2', 'mobile')

