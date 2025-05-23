from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('search/', views.search, name='search'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<slug:slug>/', views.product_list, name='category'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    # Add your URL patterns here
] 