from django import forms

from store.models import Category, Product ,ContactModel 





class ProductAddForm(forms.ModelForm):
	class Meta:
		model = Product
		exclude=('submitted_at','updated_at')