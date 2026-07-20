from django.shortcuts import render ,redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def products(request):
    return render(request, 'products.html')
def products_details(request):
    return render(request, 'products_details.html')
def cart(request):
    return render(request, 'cart.html')
def order(request):
    return render(request, 'order.html')
def women(request):
    return render(request, 'women.html')
def men(request):
    return render(request, 'men.html')
def kids(request):
    return render(request, 'kids.html')
def Accessories(request):
    return render(request, 'Accessories.html')
