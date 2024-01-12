from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("login", views.login, name='login'),
    path('login/kayit', views.kayit, name='kayit'),
    path('login/giris', views.giris, name='giris'),
    path('cart', views.cart, name='cart'),
    path('cartAdd', views.cartAdd, name='cartAdd'),
    path('cartDelete', views.cartDelete, name='cartDelete'),
    path('code', views.code, name='code'),
    #path('cart-add/<int:id>', views.cart_add, name='cart_add'),
    path('logout', views.logout, name='logout'),
    path('categories/<int:id>', views.category_detail, name='category_detail'),
    path('productSearch', views.product_search, name='productSearch'),
]