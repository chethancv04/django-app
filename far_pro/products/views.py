from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product,Cart, CartItem
from .forms import ProductForm

@login_required
def add_product(request):
    if request.user.is_seller:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.seller = request.user
                product.save()
                return redirect('product_list')
        else:   
            form = ProductForm()
        return render(request, 'products/add_product.html', {'form': form})
    else:
        return redirect('home')

@login_required
def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.user != product.seller:
        return redirect('product_list')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html', {'form': form})

@login_required
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.user == product.seller:
        product.delete()
    return redirect('product_list')

@login_required
def product_list(request):
    products = Product.objects.filter(seller=request.user)
    return render(request, 'products/product_list.html', {'products': products})


def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})
#=========================================================================
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(user=user)
    # Update the user's CustomUser.cart field
    user.cart = cart
    user.save()
    # Add product to cart or update quantity if already in cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    # Redirect to the cart page or any appropriate page
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart = cart_item.cart  # Get the cart associated with the cart item

    # Delete the cart item
    cart_item.delete()

    # Check if the cart is now empty
    if cart.cartitem_set.count() == 0:
        user = request.user
        user.cart = None  # Clear the user's cart association
        user.save()

        # Optionally, delete the cart itself if no longer needed
        cart.delete()

    # Redirect back to the cart page or any appropriate page
    return redirect('cart')

def cart(request):
    user = request.user
    cart = user.cart
    if cart:
        cart_items = cart.cartitem_set.all()
    else:
        cart_items = []
    total_amount = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_amount': total_amount,
    }
    return render(request, 'products/cart.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product_detail.html', {'product': product})
#==========================================================================
@login_required
def seller_dashboard(request):
    if request.user.is_seller:
        products = Product.objects.filter(seller=request.user)
        return render(request, 'products/seller_dashboard.html', {'products': products})
    else:
        return redirect('home')

