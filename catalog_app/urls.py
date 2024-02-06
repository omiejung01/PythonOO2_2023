from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('product_list', views.product_list, name='product list'),
    path('product_detail', views.product_detail, name='product detail'),
    path('back_login', views.back_login, name='back_login'),

]
