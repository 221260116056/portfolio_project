from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog-home'),
    path('post/<int:pk>/', views.blog_detail, name='blog-detail'),
]


