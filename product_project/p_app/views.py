from django.shortcuts import render
from .models import ProductModel,CategoryModel
from .forms import ProductForm,CategoryForm

# Create your views here.
def product(request):
    if request.method == "POST":
        data = ProductForm(request.POST)
        if data.is_valid():
            data.save()
            msg = "Product Created"
            fm = ProductForm()
            context = {
                "fm":fm,
                "msg":msg
            }
            return render(request,'home.html',context)
        else:
            msg = data
            return render(request,'home.html',{"msg":msg})
    else:
        fm = ProductForm()
        return render(request,'home.html',{"fm":fm})
    
def category(request):
    categories = CategoryModel.objects.all()
    if request.method == "POST":
        data = CategoryForm(request.POST)
        if data.is_valid():
            data.save()
            msg = "Category Created"
            fm = CategoryForm()
            context = {
                "fm":fm,
                "msg":msg,
                "categories" : categories,
            }
            return render(request,'category.html',context)
        else:
            msg = data
            return render(request,'category.html',{"msg":msg,"categories":categories})
    else:
        fm = CategoryForm()
        return render(request,'category.html',{"fm":fm,"categories":categories})