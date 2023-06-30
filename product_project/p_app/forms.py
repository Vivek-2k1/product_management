from django import forms
from .models import ProductModel,CategoryModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(queryset=ProductModel.objects.all(),widget=forms.CheckboxSelectMultiple(attrs={'class':'checkbox-inline'}),required=False,label='Products')
    class Meta:
        model = CategoryModel
        fields = "__all__"