from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from cart.cart import Cart

from .models import Order, OrderItem

def checkout(request, first_name, last_name, email, address, zipcode, state, phone, amount):
    order = Order.objects.create(first_name=first_name, last_name=last_name, email=email, address=address, zipcode=zipcode, state=state, phone=phone, amount=amount)

    for item in Cart(request):
        OrderItem.objects.create(order=order, product=item['product'], staff=item['product'].staff, price=item['product'].price, quantity=item['quantity'])
    
        order.staffs.add(item['product'].staff)

    return order

def notify_staff(order):
    from_email = settings.EMAIL_HOST_USER

    for staff in order.staffs.all():
        to_email = staff.created_by.email
        subject = 'New order'
        text_content = 'You have a new order!'
        html_content = render_to_string('email_notify_staff.html', {'order': order, 'staff': staff})

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

def notify_customer(order):
    from_email = settings.EMAIL_HOST_USER

    to_email = order.email
    subject = 'Order confirmation'
    text_content = 'Thank you for the order!'
    html_content = render_to_string('email_notify_customer.html', {'order': order})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()