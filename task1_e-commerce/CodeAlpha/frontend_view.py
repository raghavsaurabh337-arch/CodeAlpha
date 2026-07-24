from django.shortcuts import render ,redirect
from AppApi.models import Register
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
# Create your views here.'
@login_required(login_url='login') 
def home(request):
    return render(request, 'home.html')




def register(request):

    if request.method == "POST":

        Register.objects.create(
            full_name=request.POST["full_name"],
            email=request.POST["email"],
            mobile=request.POST["mobile"],
            password=request.POST["password"]
        )

        return redirect("login.html")

    return render(request, "register.html")


def login(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = Register.objects.filter(
            email=email,
            password=password
        ).first()

        if user:
            return redirect("home")

    return render(request, "login.html")








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
