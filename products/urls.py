from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("login", views.login, name='login'),
    path('products', views.products, name='products'),
    path('categories/<int:id>', views.category_detail, name='category_detail'),
    path('products/<int:id>', views.product_detail, name='product_detail'),
    path('productSearch', views.product_search, name='productSearch'),
]