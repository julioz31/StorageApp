from django.shortcuts import render, get_object_or_404, redirect
from .models import Suppliers
from .forms import SuppliersForm

def supplier_list(request):
    query = request.GET.get('q', '')
    sort_option = request.GET.get('sort', 'name')
    suppliers = Suppliers.objects.all()
    if query:
        suppliers = suppliers.filter(name__icontains=query | suppliers.filter(surname__icontains=query))

    if sort_option == 'surname':
        suppliers = suppliers.order_by('surname')
    else:
        suppliers = suppliers.order_by('name')

    return render(request, 'suppliers/supplier_list.html', {
        'suppliers': suppliers,
        'query': query,
        'sort_option': sort_option}
                  )

def edit_supplier(request, supplier_id):
    supplier = get_object_or_404(Suppliers, id=supplier_id)

    if request.method == 'POST':
        form = SuppliersForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SuppliersForm(instance=supplier)

    return render(request, 'suppliers/edit_supplier.html', {'form': form, 'supplier': supplier})

def add_supplier(request):
    if request.method == 'POST':
        form = SuppliersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SuppliersForm()

    return render(request, 'suppliers/edit_supplier.html', {'form': form})

def delete_supplier(request, supplier_id):
    supplier = get_object_or_404(Suppliers, id=supplier_id)
    supplier.delete()
    return redirect('supplier_list')

def redirect_to_products(request):
    return redirect('/products/')

