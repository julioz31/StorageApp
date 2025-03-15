from django.urls import path
from .views import edit_supplier, supplier_list, add_supplier, delete_supplier, redirect_to_products



urlpatterns = [
    path('', supplier_list, name='supplier_list'),
    path('edit/<int:supplier_id>/', edit_supplier, name='edit_supplier'),
    path('supplier/add/', add_supplier, name='add_supplier'),
    path('supplier/delete/<int:supplier_id>/', delete_supplier, name='delete_supplier'),
    path('suppliers/', redirect_to_products, name = 'redirect_to_products'),
]
