from store.models import Category, Product ,ContactModel
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def index(request):
    products =None
    category = Category.get_all_categories
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();

        
    context = {
        "products":products,
        "category" : category
    }
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact_us.html')

def contactsubmit(request):
    if request.method=='POST':
        obj=ContactModel()
        obj.name=request.POST['name']
        obj.email=request.POST['email']
        obj.message=request.POST['message']
        obj.save()
        return HttpResponse("<h1>Thanks for Contact</h1>")
    
    return render(request,'contact_us.html')