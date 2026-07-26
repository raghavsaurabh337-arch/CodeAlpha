from django.contrib import admin
from django.urls import path
from Task2_SocialMedia import front_views
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', front_views.base, name='base'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile_list, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('comment/<int:id>/', views.add_comment, name='add_comment'),
    path('post/delete/<int:id>/', views.delete_post, name='delete_post'),
    path('like/<int:id>/', views.like_post, name='like_post'),
    path('messages/', views.massage, name='massage'),
    path('reels/', views.reels, name='reels'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
