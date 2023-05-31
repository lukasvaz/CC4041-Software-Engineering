"""
URL configuration for igs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import redirect
from  main.views import home_views,transaction_views, register_view

urlpatterns = [
    path('',  lambda req:redirect('accounts/login'), name='root'),
    path("home/", home_views.home, name="home"),
    path("admin/", admin.site.urls),
    path("transaction/", transaction_views.transaction, name="transaction"),
    path("home/get-table/<str:type>", home_views.get_transactions,name="table"),
    path("registro/", register_view.register_user, name="registro"),
    path("accounts/", include("django.contrib.auth.urls"), name="accounts"),

]


