from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

from .forms import ProductForm
from .models import Product
from users.views import supplier_product_list, buyer_product_list
from users.models import Supplier, User


@login_required
@permission_required('products.can_add_product', raise_exception=True)
def add_product(request):
    # Get the supplier instance    
    supplier_user = User.objects.get(username=request.user)
    supplier = Supplier.objects.get(user=supplier_user)
    
    
    # check if the request is to add a product
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, supplier=supplier)
        if form.is_valid():
            # save the form data if is valid
            form.save()
            # redirect to a list of products that can be viewed by the supplier
            return redirect('supplier_product_list')
    
    # intialize an empty form
    else:
        form = ProductForm(supplier=supplier)

    return render(request, 'supplier/add_product.html', {'form':form})


@login_required
@permission_required('products.can_view_product', raise_exception=True)
def list_products(request):
    # check if the user is buyer, redirect to buyer product list
    # or if the user is supplier, redirect to supplier product list
    # else show all products to the admin
    if request.user.is_superuser:
        products = Product.objects.all()  # Admin sees all products
        return render(request, 'products/product_list.html', {'products': products})
    elif hasattr(request.user, 'supplier'):  # Supplier sees only their products
        supplier_product_list(request=request)
    elif hasattr(request.user, 'buyer'):  # Buyer sees in-stock products
        buyer_product_list(request=request)
    else:
        render(request, 'home.html')


@login_required
@permission_required('products.can_edit_product', raise_exception=True)
def edit_product(request, product_id):
    supplier = Supplier.objects.get(user=request.user)
    product = get_object_or_404(Product, id=product_id, supplier=supplier)
    print(request.method )
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('supplier_product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'supplier/edit_product.html', {'form': form, 'product': product})


@login_required
@permission_required('products.can_delete_product', raise_exception=True)
def delete_product(request, product_id):
    supplier = Supplier.objects.get(user=request.user)
    product = get_object_or_404(Product, id=product_id, supplier=supplier)
    print(request.method )
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('supplier_product_list')
    
    return render(request, 'supplier/delete_product.html', {'product': product})
