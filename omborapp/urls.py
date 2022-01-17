from django.urls import path
from .views import *
urlpatterns = [
    path('client/', ClientView.as_view(), name='clients'),
    path('client/', ClientView.as_view(), name='clientlar'),
    path('client_update/<int:son>/', Client_UpadteView.as_view(), name='client-update'),


    path('product/', ProductView.as_view(), name='stats'),
    path('product/', ProductView.as_view(), name='mahsulotlar'),
    path('product/', ProductView.as_view(), name='goods'),
    path('product_update/<int:son>/', Product_UpdateView.as_view(), name='product-update'),

    path('register/', RegView.as_view(), name='register'),
    path('', BulimView.as_view(), name='bolim'),
    path('logout/', LogOut, name='logout')

]