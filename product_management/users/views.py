from django.urls import reverse_lazy
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.contrib.auth import login


from products.models import Product
from .models import Supplier, User
from .forms import UserForm


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')  # Redirect to home after successful login
    def form_valid(self, form):
        login(self.request, form.get_user())  # Login user
        return super().form_valid(form)
    
    def form_invalid(self, form):

        print(form.errors)  # Print errors to console
        return super().form_invalid(form)

    
@login_required
def create_user(request):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to create users.")
        return redirect('home')  # Redirect non-admin users

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = request.POST.get('group')
            if group == 'buyer':
                user.groups.add(Group.objects.get(name='Buyers'))
            elif group == 'supplier':
                user.groups.add(Group.objects.get(name='Suppliers'))
                Supplier.objects.create(user=user, name=request.POST.get('username'))
                
            messages.success(request, f"User '{user.username}' created successfully!")
            return redirect('home')
    else:
        form = UserForm()

    return render(request, 'registration/create_user.html', {'form': form})


def is_supplier(user):
    return user.groups.filter(name='Suppliers').exists()

def is_buyer(user):
    return user.groups.filter(name='Buyers').exists()


@login_required  # Ensure that the user is logged in
def home(request):
    if request.user.is_superuser:  # Check if the user is an admin
        return redirect('admin:index')  # Redirect to the admin page
    elif is_buyer(request.user):
        return redirect('buyer_product_list')
    elif is_supplier(request.user):
        return redirect('supplier_product_list')
    return render(request, 'home.html')  # Render the home page otherwise


@login_required
@user_passes_test(is_buyer)  # Only buyers can access this
def buyer_product_list(request):
    products = Product.objects.filter(stock_status=True)
    return render(request, 'buyer/view_products.html', {'products': products})

@login_required
@user_passes_test(is_supplier)  # Only suppliers can access this
def supplier_product_list(request):
    # supplier = Supplier.objects.filter(user=request.user)
    products = Product.objects.filter(supplier=request.user.supplier)
    return render(request, 'supplier/view_products.html', {'products': products})

# @staff_member_required  # Only admin users can access
# def admin_dashboard(request):
#     return render(request, 'admin/dashboard.html')


# Cheaper analogues of their products from other suppliers
@login_required
@permission_required('products.can_view_product', raise_exception=True)
def supplier_cheaper_analogues(request):
    if not hasattr(request, 'user'):
        return redirect('list_products')

    supplier = Supplier.objects.get(user=request.user)
    supplier_products = Product.objects.filter(supplier=supplier)
    cheaper_analogues = []

    for product in supplier_products:
        # Find products from other suppliers with the same product code that are cheaper and in stock
        cheaper = Product.objects.filter(
            product_code=product.product_code,
            price__lt=product.price,
            stock_status=True
        ).exclude(supplier=request.user.supplier)
        
        if cheaper.exists():
            cheaper_analogues.append({
                'original': product,
                'cheaper_analogues': cheaper
            })
    print(cheaper_analogues)

    return render(request, 'supplier/cheaper_analogues.html', {'product_analogues': cheaper_analogues})