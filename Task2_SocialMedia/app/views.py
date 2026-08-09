from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Post, Comment



@login_required(login_url='login')
def profile_list(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    posts = Post.objects.filter(user=request.user).select_related('user__profile').order_by('-created_at')
    return render(request, "profile.html", {'profile': profile, 'posts': posts})


@login_required(login_url='login')
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "home.html", {"posts": posts})



def register(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        username = email.split('@')[0]
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        first, *last = full_name.split(' ', 1)
        user.first_name = first
        user.last_name = last[0] if last else ''
        user.save()

        Profile.objects.create(user=user)
        auth_login(request, user)
        return redirect('home')

    return render(request, "register.html")



def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
            if user:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid password.")
        except User.DoesNotExist:
            messages.error(request, "No account found with this email.")

        return redirect('login')

    return render(request, "login.html")


def logout(request):
    auth_logout(request)
    return redirect('base')


@login_required(login_url='login')
def create_post(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        caption = request.POST.get("caption")
        Post.objects.create(user=request.user, image=image, caption=caption)
        return redirect("home")
    return render(request, "create_post.html")



@login_required(login_url='login')
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "home.html", {"posts": [post]})


@login_required(login_url='login')
def add_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        comment = request.POST.get("comment")
        if comment:
            Comment.objects.create(post=post, user=request.user, comment=comment)
    return redirect("home")



@login_required(login_url='login')
def delete_post(request, id):
    post = get_object_or_404(Post, id=id, user=request.user)
    post.delete()
    return redirect('profile')



@login_required(login_url='login')
def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect("home")



@login_required(login_url='login')
def edit_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        bio = request.POST.get("bio")
        image = request.FILES.get("image")
        profile.bio = bio
        if image:
            profile.image = image
        profile.save()
        messages.success(request, "Profile updated successfully.")
        return redirect("profile")
    return render(request, "edit_profile.html", {"profile": profile})



@login_required(login_url='login')
def massage(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "massage.html", {"profiles": profiles})

@login_required(login_url='login')
def reels(request):
    posts = Post.objects.filter(image__isnull=False).exclude(image='').order_by('-created_at')
    return render(request, "reels.html", {"posts": posts})
