"""rental_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from rental_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('index/',views.index, name='index'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/',views.user_logout, name='logout'),
    path('password_change/', views.ChangePasswordResetDoneView.as_view(), name='password_change'),
    path('password_changedone', views.ChangePasswordResetDoneSuccessView.as_view(), name='password_changedone'),
    path('rental/', include('rental_app.urls')),

]