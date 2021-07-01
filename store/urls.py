from os import name
from django.urls import path

from .views import products_all,product_detail,category_list

app_name='store'
urlpatterns = [
    path('',products_all,name='products_all'),
    path('<slug:slug>/',product_detail,name='product_detail'),
    path('shop/<slug:category_slug>',category_list,name='category_list'),
    
]
