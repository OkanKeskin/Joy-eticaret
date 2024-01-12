from django.shortcuts import render
from .models import Category,Product

kategoriler = ["tshirt", "sweatshirt", "mont", "kazak", "pantolon", "ayakkabi", "canta", "aksesuar"]
urun_listesi = [
    {
        "film_adi": "The Godfather",
        "yil": 1972,
        "puan": 9.2,
        "kategori": "drama",
        "anasayfa": True
    },
    {
        "film_adi": "The Shawshank Redemption",
        "yil": 1994,
        "puan": 9.3,
        "kategori": "drama",
        "anasayfa": False
    }
]

def home(request):
    data = {
        "kategoriler" : Category.objects.all(),
        "veritabanı" : Product.objects.filter(anasayfa=True).all()[:3],
        "urun_listesi_electronics": Product.objects.filter(category_id=1).all()[:3],
        "urun_listesi_accessories": Product.objects.filter(category_id=2).all()[:3],
        "urun_listesi_fashion": Product.objects.filter(category_id=3).all()[:3],
        "urun_listesi_stationary": Product.objects.filter(category_id=4).all()[:3],
        "urun_listesi_cosmatic": Product.objects.filter(category_id=5).all()[:3],
    }
    return render(request, 'index.html', data)

def products(request):
    data = {
        "kategoriler": kategoriler,
        "urun_listesi": urun_listesi
    }
    return render(request, 'products.html',data)

def product_detail(request, id):
    data = {
        "kategoriler": kategoriler,
        "urun_listesi": urun_listesi,
        "id": id
    }
    return render(request, 'product_detail.html', data)

def login(request):
    return render(request, 'login.html')

def category_detail(request, id):
    query = request.GET.get('order')
    if(query):
        if(query == "asc"):
            data = {
                "id": id,
                "kategoriler": Category.objects.all(),
                "kategori_name" : Category.objects.get(id=id).name,
                "urunler": Product.objects.filter(category_id=id).all().order_by('price'),
            }
        else:
            data = {
                "id": id,
                "kategoriler": Category.objects.all(),
                "kategori_name" : Category.objects.get(id=id).name,
                "urunler": Product.objects.filter(category_id=id).all().order_by('-price'),
            }
    else:
        data = {
            "id": id,
            "kategoriler": Category.objects.all(),
            "kategori_name" : Category.objects.get(id=id).name,
            "urunler": Product.objects.filter(category_id=id).all(),
        }
    return render(request, 'category_detail.html', data)

def product_search(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Product.objects.filter(name__icontains=query).all()

    context = {
        'query': query,
        'results': results,
        'kategoriler': Category.objects.all(),
    }

    return render(request, 'productSearch.html', context)
