from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.views import View

from .models import *

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        log = request.POST['login']
        parol = request.POST['password']
        user = authenticate(username=log, password=parol)
        if user is None:
            return redirect('login')
        else:
            login(request, user)
            return redirect('/bolim')

def LogOut(request):
    logout(request)
    return redirect('login')

class RegView(View):
     def get(self, request):
         return render(request, 'register.html')


class BulimView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'bulimlar.html')
        else:
            return redirect('login')

class ClientView(View):
    def get(self, request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            clients = Client.objects.filter(ombor=o)
            return render(request, 'clients.html', {'all_clients': clients})
        else:
            return redirect('login')

    def post(self, request):
        o = Ombor.objects.get(user=request.user)
        Client.objects.create(
            ism=request.POST['client_name'],
            tel=request.POST['client_phone'],
            dokon_nomi=request.POST['client_shop'],
            joylashuv=request.POST['client_address'],
            qarz=request.POST['client_qarz'],
            ombor=o
        )
        return redirect('clientlar')

class Client_UpadteView(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            clients = Client.objects.get(id=son)
            return render(request, 'client_update.html', {'client': clients})
        else:
            return redirect('login')

    def post(self, request, son):
        if request.user.is_authenticated:
            client = Client.objects.get(id=son)
            client.ism = request.POST['client_name']
            client.tel = request.POST['client_phone']
            client.dokon_nomi = request.POST['client_shop']
            client.joylashuv = request.POST['client_address']
            client.qarz = request.POST['client_qarz']
            client.save()
            return redirect('clientlar')
        else:
            return redirect('login')



class ProductView(View):
    def get(self, request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            products = Product.objects.filter(ombor=o)
            return render(request, 'products.html', {'all_products': products})
        else:
            return redirect('login')

    def post(self, request):
        o = Ombor.objects.get(user=request.user)
        Product.objects.create(
            nom=request.POST['pr_name'],
            brend_nomi=request.POST['pr_brand'],
            narx=request.POST['pr_price'],
            miqdor=request.POST['pr_amount'],
            ombor=o
        )
        return redirect('mahsulotlar')


class Product_UpdateView(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            products = Product.objects.get(id=son)
            return render(request, 'product_update.html', {'product': products})
        else:
            return redirect('login')

    def post(self, request, son):
        if request.user.is_authenticated:
            product = Product.objects.get(id=son)
            product.nom = request.POST['name']
            product.brend_nomi = request.POST['brand_name']
            product.narx = request.POST['price']
            product.miqdor = request.POST['amount']
            product.save()
            return redirect('mahsulotlar')
        else:
            return redirect('login')





