from django.conf.urls import url
from rental_app import views
from django.contrib import admin
from django.urls import path

app_name= 'rental_app'
urlpatterns = [

    path('book/', views.book_list, name='book_list'),
    path('book_update/<int:id>', views.book_update, name='book_update'),
    path('book_add/', views.book_add, name='book_add'),
    path('book_delete/<int:id>', views.book_delete, name='book_delete'),


    path('customer/', views.customer_add, name='customer'),
    path('customer_update/<int:id>', views.customer_update, name='customer_update'),
    path('customer_delete/<int:id>', views.customer_delete, name='customer_delete'),
    path('customer_display_info/<int:id>', views.customer_display_info, name='customer_display_info'),

        ]
