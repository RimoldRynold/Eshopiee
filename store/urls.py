from django.urls import path
from .views import index,contact,contactsubmit,signup,Login


urlpatterns = [
    path('',index,name='home'),
    path('contact',contact,name='contact'),
    path('contactsubmit',contactsubmit,name='contactsubmit'),

    path('signup',signup,name='signup'),
    # path('login1',views.login1,name='login1'),
    path('login1',Login.as_view(),name='login1'),
]
