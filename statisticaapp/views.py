from django.shortcuts import render, redirect
from django.views import View

from .models import Stats
from omborapp.models import Ombor, Client, Product


class StatsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            C = Client.objects.filter(ombor=o)
            p = Product.objects.filter(ombor=o)
            s = Stats.objects.all().order_by('-sanasi')
            return render(request, 'stats.html', {"all_stats": s, "products": p, "clients": C})
        else:
            return redirect('login')
    def post(self, request):
        a = Ombor.objects.get(user=request.user)
        p = request.POST['product']
        m = request.POST['miqdor']
        c = request.POST['client']
        n = request.POST['nasiya']
        # u = request.POST["summa"],
        # t  = request.POST["tolandi"],
        # n = u - t

        Stats.objects.create(
            product=Product.objects.get(id=p),
            client=Client.objects.get(id=c),
            sanasi=request.POST["sana"],
            miqdor=request.POST['miqdor'],
            umumiy_summa=request.POST["summa"],
            tolandi=request.POST["tolandi"],
            nasiya=n,
            ombor=a
        )
        pro = Product.objects.get(id=p)
        pro.miqdor=int(pro.miqdor) - int(m)
        pro.save()
        cl = Client.objects.get(id=c)
        cl.qarz = int(cl.qarz) + int(n)
        cl.save()
        return redirect('stats')

