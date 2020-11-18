from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from rental_app.models import BedType, Book, Customer
from rental_app.forms import UserForm, FormBook, FormCustomer
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout  # for later
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.forms import formset_factory
from django.forms import modelformset_factory
from django.contrib.auth import views as auth_views, forms as auth_forms
from django.urls import reverse_lazy


def user_logout(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (user_login, request.path))

    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print('someone tried to login and failed :(')
            print('username: {} password: {}'.format(username, password))
            return HttpResponse('invalid login details supplied')

    else:
        return render(request, 'login.html', {})


def index(request):
    return render(request, 'index.html')

@login_required(login_url='user_login')
def book_list(request):
        book_list = Book.objects.order_by('check_in')
        book = {'book': book_list}
        return render(request, 'book_list.html', context=book)

@login_required(login_url='user_login')
def book_update(request, id):
    instance = get_object_or_404(Book, id=id)
    book_form = FormBook(instance=instance)
    if request.method == "POST":
        book_form = FormBook(data=request.POST, instance=instance)
        if book_form.is_valid():
            book = book_form.save()
            book.save()
            messages.add_message(request, messages.SUCCESS,'Booking was updated successfully')
            return redirect('rental_app:book_list')
        else:
            print(book_form.errors)
    else:  # http request
        book_form = FormBook(instance=instance)
    return render(request, 'book_update.html', {'book_form': book_form, 'book': instance})

@login_required(login_url='user_login')
def book_add(request):
    if request.method == "POST":
        book_form = FormBook(data=request.POST)
        if book_form.is_valid():
            book_form.save()
            messages.add_message(request, messages.SUCCESS,'Booking was added successfully')
            return redirect('rental_app:book_list')
        else:
            print(book_form.errors)
    else:  # http request
        book_form = FormBook()
    return render(request, 'book_update.html', {'book_form': book_form,})

@login_required(login_url='user_login')
def book_delete(request, id):
    instance = get_object_or_404(Book, id=id)
    instance.delete()
    messages.add_message(request, messages.SUCCESS,'Booking was deleted successfully')
    return HttpResponseRedirect(reverse('rental_app:book_list'))


# ================================================================================


@login_required(login_url='user_login')
def customer_update(request, id):
    instance = get_object_or_404(Customer, id=id)
    customer_form = FormCustomer(instance=instance)
    if request.method == "POST":
        customer_form = FormCustomer(data=request.POST, instance=instance)
        if customer_form.is_valid():
            customer_form.save()
            messages.add_message(request, messages.SUCCESS,'Customer was updated successfully')
            return redirect('rental_app:customer')
        else:
            print(customer_form.errors)
    else:  # http request
        customer_form = FormCustomer(instance=instance)
    return render(request, 'customer_update.html', {'customer_form': customer_form, 'customer': instance})

@login_required(login_url='user_login')
def customer_delete(request, id):
    instance = get_object_or_404(Customer, id=id)
    instance.delete()
    messages.add_message(request, messages.SUCCESS,'Customer was deleted successfully')
    return HttpResponseRedirect(reverse('rental_app:customer'))

@login_required(login_url='user_login')
def customer_add(request):
    CustomerFormSet = modelformset_factory(Customer,form=FormCustomer,fields=('__all__'), extra=3)
    form = CustomerFormSet(queryset=Customer.objects.none())
    if request.method == 'POST':
        form = CustomerFormSet(request.POST)
        if form.is_valid():
            form.save()
            form = CustomerFormSet(queryset=Customer.objects.none())
    # display all customer
    queryset = Customer.objects.all().order_by('first_name')
    context = {'customer':queryset,'form': form}
    return render(request, 'customer_list.html', context)

@login_required(login_url='user_login')
def customer_display_info(request, id):
    instance=get_object_or_404(Customer, id=id)

    return render(request, 'customer_display_info.html', {'instance': instance})

class ChangePasswordResetDoneView(auth_views.PasswordChangeView):
    form_class = auth_forms.PasswordChangeForm
    template_name = 'password_change.html'
    success_url = reverse_lazy('password_changedone')

class ChangePasswordResetDoneSuccessView(auth_views.PasswordChangeView):
    form_class = auth_forms.PasswordChangeForm
    template_name = 'password_changedone.html'
