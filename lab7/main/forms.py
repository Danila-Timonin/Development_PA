from django import forms
from .models import Visitor, Store, Product, Purchase, Review


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ('name', 'email')


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name', 'location')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description')


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['visitor', 'store', 'purchase_date', 'amount']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['visitor', 'product', 'rating', 'comment']
        widgets = {
            'visitor': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
