

from django.shortcuts import render, redirect
from AppApi.models import Register, Product
from django.contrib.auth.hashers import make_password, check_password



def home(request):

    data = Product.objects.all()
    return render(request, "home.html", {"data": data})


def register(request):

    if request.method == "POST":

        password = request.POST["password"]

        Register.objects.create(
            full_name=request.POST["full_name"],
            email=request.POST["email"],
            mobile=request.POST["mobile"],
            password=make_password(password)
        )

        return redirect("login")

    return render(request, "register.html")


def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = Register.objects.filter(email=email).first()

        if user and check_password(password, user.password):

            request.session["user_id"] = user.id
            request.session["user_email"] = user.email

            return redirect("home")

        return render(request, "login.html", {"error": "Invalid email or password"})

    return render(request, "login.html")


def products(request):
    data = Product.objects.all()
    return render(request, "products.html", {"data": data})


def products_details(request):
    
    return render(request, "products_details.html")


def cart(request):
    return render(request, "cart.html")


def order(request):
    return render(request, "order.html")


def women(request):
    return render(request, "women.html")


def men(request):
    return render(request, "men.html")


def kids(request):
    return render(request, "kids.html")


def Accessories(request):
    return render(request, "Accessories.html")
