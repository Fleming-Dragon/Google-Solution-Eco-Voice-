
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('customer.urls')),
    path('charity/',include('charity_user.urls'))
]
