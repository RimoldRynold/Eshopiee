from django.urls import path
from adminpanel.views import *


urlpatterns = [
    path('',admin.as_view(),name='admin'),
    path('products',products.as_view(),name='products'),
    
    path('productadd',ProductAdd.as_view(),name='productadd'),
    path('listproduct',listproduct.as_view(),name='listproduct'),

    path('deleteproduct/(?P<pk>[0-9]+)/$',deleteproduct.as_view(),name='deleteproduct'),
    path('productdetail/(?P<pk>[0-9]+)/$',productdetail.as_view(),name='productdetail'),

    path('listfeedback/',listfeedback.as_view(),name='listfeedback'),

    path('<pk>/update',ProductUpdate.as_view(),name='update'),
    path('<pk>/orderupdate',OrderUpdate.as_view(),name='orderupdate'),
]
