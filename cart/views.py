from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect,render
from django.conf import settings
from . import forms
from order.models import Order
from django.contrib import messages
from .cart import Cart
from .forms import CheckoutForm
from order.utilities import checkout, notify_customer, notify_staff


def cart_detail(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)
    form = CheckoutForm()
    if request.method == 'POST':
        form=CheckoutForm(request.POST)

        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']

            order = checkout(request, first_name, last_name, email, address, zipcode, state, phone, cart.get_total_cost())
            
            # notify_customer(order)
            # notify_staff(order)
            form = form.save()
            
            return render(request,'make_payment.html',{'form':form,'paystack_public_key':settings.PAYSTACK_PUBLIC_KEY})
                           
    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart.remove(remove_from_cart)

        return redirect('cart')
    
    if change_quantity:
        cart.add(change_quantity, quantity, True)

        return redirect('cart')
    return render(request, 'cart.html', {'form': form})


def verify_payment(request: HttpRequest, ref:str) -> HttpResponse:
    cart = Cart(request)
    payment = get_object_or_404(Order, ref=ref)
    if request.method == 'POST':
        cart.clear()
    else:
        cart.clear()
    return render(request,'success.html')