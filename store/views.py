from store.models import Category, Product ,ContactModel , Customer ,Order
from django.shortcuts import redirect, render

from django.http import HttpResponse

from django.contrib.auth.hashers import make_password,check_password

from store.middlewares.auth import auth_middleware#the decoratoe is used when it is used inside the function.here is the class. so it needs a method decorator
from django.utils.decorators import method_decorator

from django.views import View
# Create your views here.

'''
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
        "category" : category,
        
    }
    print('you are :' , request.session.get('email'))
    return render(request,'index.html',context)
'''

class Index(View):
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products =None
        #request.session.get('cart').clear()
        category = Category.get_all_categories
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();

            
        context = {
            "products":products,
            "category" : category,
            
        }
        print('you are :' , request.session.get('email'))
        return render(request,'index.html',context)

    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart',request.session['cart'])
        return redirect('home')



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
'''
def validateCustomer(customer):
    error_message = None;
    if not customer.first_name:
        error_message = 'First Name Required !!'
    # elif len(firstname) < 4 :
    #     error_message = 'First Name must be 4 or more character long'
    elif not customer.last_name:
        error_message = 'Last Name Required !!'
    elif not customer.phone  :
        error_message = 'Phone Number Required'
    elif len(customer.phone) <10 :
        error_message = 'Phone must be 10 character long'
    elif not customer.password  :
        error_message = 'Password Number Required'
    # elif len(password) <6 :
    #     error_message = 'Passwors must be 6 or more character long'
    elif customer.isExists():
        error_message = 'Email address already registered..'

    return error_message

def registerUser(request):
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

    customer = Customer(first_name=firstname,
        last_name=lastname,
        phone = phone,
        email = email,
        password = password
        )
    error_message = validateCustomer(customer)
    
    #saving
    if not error_message:
        print(firstname,lastname,phone,email,password)
        customer.password = make_password(customer.password)
        customer.register()
        # return redirect('/') or
        return redirect('home')
    else:
        data = {
            'values' : value,
            'error' : error_message,
        }
        return render(request,'signup.html',data)
    

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')

    else:
        return registerUser(request)
'''
class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
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

        customer = Customer(first_name=firstname,
            last_name=lastname,
            phone = phone,
            email = email,
            password = password
            )
        error_message = self.validateCustomer(customer)
        
        #saving
        if not error_message:
            print(firstname,lastname,phone,email,password)
            customer.password = make_password(customer.password)
            customer.register()
            # return redirect('/') or
            return redirect('home')
        else:
            data = {
                'values' : value,
                'error' : error_message,
            }
            return render(request,'signup.html',data)

    def validateCustomer(self,customer):
        error_message = None;
        if not customer.first_name:
            error_message = 'First Name Required !!'
        # elif len(firstname) < 4 :
        #     error_message = 'First Name must be 4 or more character long'
        elif not customer.last_name:
            error_message = 'Last Name Required !!'
        elif not customer.phone  :
            error_message = 'Phone Number Required'
        elif len(customer.phone) <10 :
            error_message = 'Phone must be 10 character long'
        elif not customer.password  :
            error_message = 'Password Number Required'
        # elif len(password) <6 :
        #     error_message = 'Passwors must be 6 or more character long'
        elif customer.isExists():
            error_message = 'Email address already registered..'

        return error_message


class Login(View):
    def get(self,request):
        return render(request,'login1.html')
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        print(customer)
        error_message = None
        if customer:#here is the code to proceed only after getting the customer(check get_customer_by_email 1st )
            print(customer)
            flag = check_password(password,customer.password)#customer.password-encoded password
            if flag:
                # request.session['customer_id'] = customer.id
                request.session['customer'] = customer.id
                # request.session['email'] = customer.email
                return redirect('home')
            else:
                error_message = 'Email or Password invalid !!!'

        else:
            error_message = 'Email or Password invalid !!!'
        
        return render(request,'login1.html',{'error':error_message})


def logout(request):
    request.session.clear()
    return redirect('login1')

class Cart(View):
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request,'cart.html',{'products' : products})

class CheckOut(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')#customer-it is customer id
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address , phone , customer , cart , products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer =Customer(id= customer),
            product = product,
            price = product.price,
            address = address,
            phone = phone,
            quantity = cart.get(str(product.id)))

            order.save()

        request.session['cart'] = {}

        return redirect('cart')

class OrderView(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request,'orders.html',{'orders':orders})

'''
def login1(request):
    if request.method == 'GET':
        return render(request,'login1.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        print(customer)
        error_message = None
        if customer:#here is the code to proceed only after getting the customer(check get_customer_by_email 1st )
            print(customer)
            flag = check_password(password,customer.password)#customer.password-encoded password
            if flag:
                return redirect('home')
            else:
                error_message = 'Email or Password invalid !!!'

        else:
            error_message = 'Email or Password invalid !!!'
        
        return render(request,'login1.html',{'error':error_message})

'''