from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('contact',views.contact,name='contact'),
    path('contactsubmit',views.contactsubmit,name='contactsubmit'),

    path('signup',views.signup,name='signup'),
    path('login1',views.login1,name='login1'),
]
