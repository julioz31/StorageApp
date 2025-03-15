from django.urls import path
from .views import product_list, edit_product, edit_category, create_category, delete_category, create_product, delete_product, redirect_to_suppliers
from django.shortcuts import redirect
urlpatterns = [
    path('', product_list, name='product_list'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('category/edit/<int:category_id>/', edit_category, name='edit_category'),
    path('category/add/', create_category, name='create_category'),
    path('category/delete/<int:category_id>/', delete_category, name='delete_category'),
    path('product/add/', create_product, name='create_product'),
    path('product/delete/<int:product_id>/', delete_product, name='delete_product'),
    path('suppliers/', redirect_to_suppliers, name = 'redirect_to_suppliers'),
]