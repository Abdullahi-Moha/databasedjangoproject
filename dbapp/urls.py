from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),  # Homepage for blog list
    path('blog_detail/', views.blog_detail, name='blog_detail'),  # Correct view name
]

