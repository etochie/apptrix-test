from django import forms


class OrderForm(forms.Form):
    email = forms.EmailField()
