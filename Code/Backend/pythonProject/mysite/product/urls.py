from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('product=<int:id>/', views.showProduct, name = 'product'),
    path('search=<str:name>/', views.search, name = 'search'),
    path('contact/', views.showContact, name = 'contact'),
    path('profile/', views.editProfile, name = 'profile'),
    path('Type=<str:type>&Order=<str:order>&Filter=<str:filter>/', views.showAllProduct, name='type_order_filter'),
    path('Type=<str:type>&Filter=<str:filter>/', views.showAllProduct, name='type_filter'),
    path('Type=<str:type>&Order=<str:order>/', views.showAllProduct, name='type_order'),
    path('Type=<str:type>/', views.showAllProduct, name='type'),
    path('<str:str>/', views.show, name='show'),

]