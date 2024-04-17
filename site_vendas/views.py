from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'site_vendas/index.html')

def produto(request):
    return render(request,'site_vendas/Produto1.html')

def cart(request):
    return render(request,'site_vendas/cart.html')