from django.db import models
from django.shortcuts import render

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200,default='',blank=True)
    image = models.ImageField(upload_to='products/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)


    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();


class ContactModel(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500 )
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def register(self):
        self.save()
    '''
    @staticmethod
    def get_customer_by_email(email):
        return Customer.objects.get(email = email)here is the code to proceed only after getting the customer,if you no longer have customer,"Customer matching query does not exist." error will come , to avoid that error we are writing code in try except block'''

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        
        return False

    def __str__(self):
        return self.first_name