from django import forms
from .models import Suppliers

class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = ['name', 'surname', 'po_batkovi','contact_info']
