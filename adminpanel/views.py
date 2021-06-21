from django.shortcuts import render,redirect

from django.views.generic import View,TemplateView 
from django.views.generic.edit import UpdateView

from store.models import Category, Product ,ContactModel ,Customer ,Order 

from adminpanel.forms import ProductAddForm , OrderAddForm
# Create your views here.


class admin(TemplateView):
	template_name= 'admin.html'

# class products(TemplateView):
# 	template_name= 'products.html'

class products(View):
	template_name = 'products.html'
	model= Product

	def get(self,request):
		count1 = Product.objects.latest('submitted_at')
		count = Product.objects.all().count()
		mydictionary ={
			'count' : count,
			'count1' : count1
		}
		return render(request,self.template_name,mydictionary)


class ProductAdd(View):
	template_name = 'product_add.html'
	form_class= ProductAddForm

	def get(self,request):
		form = self.form_class()
		mydictionary ={
			'form' : form
		}
		return render(request,self.template_name,mydictionary)


	def post(self,request):
		form = self.form_class(request.POST,request.FILES)
		if form.is_valid():
			cat_obj = Category.objects.get(id=request.POST.get('category'))
			product_obj = Product.objects.create(
				category = cat_obj,
				name = request.POST.get('name'),
				price = request.POST.get('price'),
				description = request.POST.get('description'),
				image = request.FILES.get('image')
				)
			return redirect('/dash/products')
		else:
			form = self.form_class()
			return render(request,self.template_name,{'form':form})


class listproduct(View):
	template_name = 'list_product.html'
	
	def get(self,request):
		product = Product.objects.all()
		mydictionary={
			'cat': product
		}
		return render(request,self.template_name,mydictionary)


class deleteproduct(View):
	template_name = 'list_product.html'

	def get(self,request,pk):
		cat_obj = Product.objects.get(id=pk).delete()
		products = Product.objects.all()
		mydictionary={
			'cat': products
		}
		return render(request,self.template_name,mydictionary)


class productdetail(View):
	template_name = 'product_detail.html'

	def get(self,request,pk):
		obj = Product.objects.get(id=pk)
		mydictionary={
			'cat': obj
		}
		return render(request,self.template_name,mydictionary)
    
class listfeedback(View):
	template_name = 'list_feedback.html'
	
	def get(self,request):
		feed = ContactModel.objects.all()
		mydictionary={
			'cat': feed
		}
		return render(request,self.template_name,mydictionary)

class ProductUpdate(UpdateView):
	template_name= 'product_update.html'
	model= Product
	fields = ['name','price','category','description','image']
	success_url= '/dash/listproduct'

class OrderUpdate(UpdateView):
	template_name= 'order_update.html'
	model= Order
	fields = ['product','customer','quantity','price','address','phone','status']
	success_url= '/dash/listproduct'