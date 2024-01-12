from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart, Category,Product,User

def home(request):
    if request.session.get('giris') == True:
        data = {
            "giris" : True,
            "user_name" : request.session.get('user_name'), # "user_name" : "Ahmet
            "kategoriler" : Category.objects.all(),
            "veritabanı" : Product.objects.filter(anasayfa=True).all()[:3],
            "urun_listesi_electronics": Product.objects.filter(category_id=1).all()[:3],
            "urun_listesi_accessories": Product.objects.filter(category_id=2).all()[:3],
            "urun_listesi_fashion": Product.objects.filter(category_id=3).all()[:3],
            "urun_listesi_stationary": Product.objects.filter(category_id=4).all()[:3],
            "urun_listesi_cosmatic": Product.objects.filter(category_id=5).all()[:3],
        }
    else:
        data = {
            "giris" : False,
            "kategoriler" : Category.objects.all(),
            "veritabanı" : Product.objects.filter(anasayfa=True).all()[:3],
            "urun_listesi_electronics": Product.objects.filter(category_id=1).all()[:3],
            "urun_listesi_accessories": Product.objects.filter(category_id=2).all()[:3],
            "urun_listesi_fashion": Product.objects.filter(category_id=3).all()[:3],
            "urun_listesi_stationary": Product.objects.filter(category_id=4).all()[:3],
            "urun_listesi_cosmatic": Product.objects.filter(category_id=5).all()[:3],
        }
    return render(request, 'index.html', data)

def login(request):
    return render(request, 'login.html')

def category_detail(request, id):
    query = request.GET.get('order')
    if request.session.get('giris') == True:
        if(query):
            if(query == "asc"):
                data = {
                    "giris" : True,
                    "user_name" : request.session.get('user_name'), # "user_name" : "Ahmet
                    "id": id,
                    "kategoriler": Category.objects.all(),
                    "kategori_name" : Category.objects.get(id=id).name,
                    "urunler": Product.objects.filter(category_id=id).all().order_by('price'),
                }
            else:
                data = {
                    "giris" : True,
                    "user_name" : request.session.get('user_name'), # "user_name" : "Ahmet
                    "id": id,
                    "kategoriler": Category.objects.all(),
                    "kategori_name" : Category.objects.get(id=id).name,
                    "urunler": Product.objects.filter(category_id=id).all().order_by('-price'),
                }
        else:
            data = {
                "giris" : True,
                "user_name" : request.session.get('user_name'), # "user_name" : "Ahmet
                "id": id,
                "kategoriler": Category.objects.all(),
                "kategori_name" : Category.objects.get(id=id).name,
                "urunler": Product.objects.filter(category_id=id).all(),
            }
    else:
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

    if request.session.get('giris') == True:
        context = {
            'giris' : True,
            'user_name' : request.session.get('user_name'), # "user_name" : "Ahmet
            'query': query,
            'results': results,
            'kategoriler': Category.objects.all(),
        }
    else:
        context = {
            'query': query,
            'results': results,
            'kategoriler': Category.objects.all(),
        }

    return render(request, 'productSearch.html', context)

def kayit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User(name=name, email=email, password=password)
        user.save()
    return redirect('home')

def cart(request):
    list = []
    if request.session.get('giris') == True:
        if request.session.get('cart') != None:
            for i in request.session.get('cart'):
                list.append(Product.objects.get(id=i))
        data = {
            "giris" : True,
            "user_name" : request.session.get('user_name'), # "user_name" : "Ahmet
            "kategoriler" : Category.objects.all(),
        }
        data["list"] = list
    else:
        data = {
            "giris" : False,
            "kategoriler" : Category.objects.all(),
        }
        data["list"] = list
    return render(request, 'cart.html', data)

    

def giris(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email, password=password).first()
        if user:
            request.session['giris'] = True
            request.session['user_name'] = user.name
            return redirect('home')
    messages.error(request, 'Email veya şifre hatalı!')
    return redirect('login')

def logout(request):
    request.session['giris'] = False
    request.session['user_name'] = ""
    return redirect('home')

def cartAdd(request):
    id = request.GET.get('id')
    if request.session.get('giris') == True:
        if request.session.get('cart') == None:
            request.session['cart'] = []
        request.session['cart'].append(id)
        request.session.modified = True
        return redirect('cart')
    else:
        messages.error(request, 'Lütfen giriş yapınız!')
    return redirect('cart')


def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.add(product=product,
             quantity=1,
             override_quantity=False)
    return redirect('home')

def cart_detail(request):
    cart = Cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'cart.html', context=context)