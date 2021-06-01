from store.models import Category, Product ,ContactModel , Customer
from django.shortcuts import redirect, render

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

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        value = {
            'firstname' : firstname,
            'lastname' : lastname,
            'phone' : phone,
            'email' : email,
            'password' :password
        }
        #valiadation
        error_message = None
        if not firstname:
            error_message = 'First Name Required !!'
        # elif len(firstname) < 4 :
        #     error_message = 'First Name must be 4 or more character long'
        elif not lastname:
            error_message = 'Last Name Required !!'
        elif not phone  :
            error_message = 'Phone Number Required'
        elif len(phone) <10 :
            error_message = 'Phone must be 10 character long'
        elif not password  :
            error_message = 'Password Number Required'
        # elif len(password) <6 :
        #     error_message = 'Passwors must be 6 or more character long'

        #saving
        if not error_message:
            print(firstname,lastname,phone,email,password)
            customer = Customer(first_name=firstname,
            last_name=lastname,
            phone = phone,
            email = email,
            password = password
            )
            customer.register()
            # return redirect('/') or
            return redirect('home')
        else:
            data = {
                'values' : value,
                'error' : error_message,
            }
            return render(request,'signup.html',data)