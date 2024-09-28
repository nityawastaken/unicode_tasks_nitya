# """
# URL configuration for task1 project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include
# from blog import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('create/', views.create_blog_post, name='create_blog_post'),
#     # path('', views.blog_list, name='blog_list'),
#     # path('<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
#     # path('<int:pk>/edit/', views.update_blog_post, name='update_blog_post'),
#     # path('<int:pk>/delete/', views.delete_blog_post, name='delete_blog_post'),
#     path('', views.blog_list, name='blog_list'),  # List all blog posts
#     path('post/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),  
#     path('post/new/', views.create_blog_post, name='create_blog_post'), 
#     path('post/<int:pk>/edit/', views.update_blog_post, name='update_blog_post'),  
#     path('post/<int:pk>/delete/', views.delete_blog_post, name='delete_blog_post'),  
# ]

from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('update/<int:pk>/', views.update_blog_post, name='update_blog_post'),
    path('delete/<int:pk>/', views.delete_blog_post, name='delete_blog_post'),
    path('<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
    path('', views.blog_list, name='blog_list'),
]
