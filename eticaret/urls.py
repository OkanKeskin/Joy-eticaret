from django.contrib import admin
from django.urls import path,include

#/ = Home page
#/products/ = List products
#/products/1/ = Detail products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
]
