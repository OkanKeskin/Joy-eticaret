from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    anasayfa = models.BooleanField(default=False)
    description = models.TextField(default="")
    imageUrl = models.CharField(max_length=255, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"

class DiscountCode(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=255)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.code}"

