from django.urls import path

from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart'),
    path('<str:ref>/', views.verify_payment, name='verify-payment'),

]