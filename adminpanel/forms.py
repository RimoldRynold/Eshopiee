from django import forms

from store.models import Category, Product ,ContactModel ,Customer ,Order





class ProductAddForm(forms.ModelForm):
	class Meta:
		model = Product
		exclude=('submitted_at','updated_at')
		
class OrderAddForm(forms.ModelForm):
	class Meta:
		model = Order
		exclude=('date',)