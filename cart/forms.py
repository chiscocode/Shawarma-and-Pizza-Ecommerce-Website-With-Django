from django import forms
from order.models import Order


class CheckoutForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=("first_name","last_name","address","zipcode","state","phone","amount","email",)