from django.contrib import admin
from .models import Category,Product,User,Cart,DiscountCode

admin.site.register(Category, list_display=['name'])
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(DiscountCode)
