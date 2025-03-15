from django import forms
from .models import Product, Category

from django import forms
from .models import Product
from suppliers.models import Suppliers, SupplierProduct

class ProductForm(forms.ModelForm):
    suppliers = forms.ModelMultipleChoiceField(
        queryset=Suppliers.objects.all(),
        widget=forms.SelectMultiple,
        required=False,
        label="Постачальники"
    )

    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'image']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        if self.instance.pk:  # Якщо продукт існує
            self.fields['suppliers'].initial = Suppliers.objects.filter(
                supplierproduct__product=self.instance
            )

    def save(self, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save()
            self.instance.supplierproduct_set.all().delete()  # Видаляємо старі зв’язки
            for supplier in self.cleaned_data['suppliers']:
                SupplierProduct.objects.create(supplier=supplier, product=product)  # Додаємо нові
        return product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']