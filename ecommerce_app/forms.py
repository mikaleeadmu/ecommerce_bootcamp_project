from django import forms

class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=255)
    payment_info = forms.CharField(max_length=100)