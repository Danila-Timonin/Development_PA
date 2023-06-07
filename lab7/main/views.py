from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import VisitorForm, StoreForm, ProductForm, PurchaseForm, ReviewForm
from .models import Visitor, Store, Purchase, Product, Review


def index(request):
    visitor = Visitor.objects.all()
    return render(request, 'main/visitor.html', {'visitors': visitor})


def visitor_create(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VisitorForm()
    return render(request, 'main/visitor_create.html', {'form': form})


def visitor_update(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        form = VisitorForm(request.POST, instance=visitor)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VisitorForm(instance=visitor)
    return render(request, 'main/visitor_update.html', {'form': form, 'visitor': visitor})


def visitor_delete(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        visitor.delete()
        return redirect('home')
    return render(request, 'main/visitor_delete.html', {'visitor': visitor})


def store(request):
    store = Store.objects.all()
    return render(request, 'main/store.html', {'store': store})


def store_create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = StoreForm()
    return render(request, 'main/store_create.html', {'form': form})


def store_update(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = StoreForm(instance=store)
    return render(request, 'main/store_update.html', {'form': form, 'store': store})


def store_delete(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        store.delete()
        return redirect('store')
    return render(request, 'main/store_delete.html', {'store': store})


def product(request):
    product = Product.objects.all()
    return render(request, 'main/product.html', {'products': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm()
    return render(request, 'main/product_create.html', {'form': form})


def product_update(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = StoreForm(instance=store)
    return render(request, 'main/store_update.html', {'form': form, 'store': store})


def product_delete(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        store.delete()
        return redirect('store')
    return render(request, 'main/store_delete.html', {'store': store})


def purchase(request):
    purchase = Purchase.objects.all()
    return render(request, 'main/purchase.html', {'purchase': purchase})


def purchase_create(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase')
    else:
        form = PurchaseForm()
    return render(request, 'main/purchase_create.html', {'form': form})


def purchase_update(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            return redirect('purchase')
    else:
        form = PurchaseForm(instance=purchase)
    return render(request, 'main/purchase_update.html', {'form': form})


def purchase_delete(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    if request.method == 'POST':
        purchase.delete()
        return redirect('purchase')
    return render(request, 'main/purchase_delete.html', {'purchase': purchase})


def review(request):
    reviews = Review.objects.all()
    return render(request, 'main/review.html', {'reviews': reviews})


def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review')
    else:
        form = ReviewForm()
    return render(request, 'main/review_create.html', {'form': form})


def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'main/review_update.html', {'form': form, 'review': review})


def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('review')
    return render(request, 'main/review_delete.html', {'review': review})