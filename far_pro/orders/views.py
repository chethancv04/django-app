from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Order, OrderItem
from products.models import Product
from django.contrib.auth.decorators import login_required



@login_required
def place_order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = request.user 
    # Perform any payment processing logic here (dummy process)
    payment_details = "Payment received via XYZ method."
    # Create the order with 'pending' status
    order = Order.objects.create(
        user=user,
        total_amount=product.price,
        payment_details=payment_details,
        status='pending'
    )
    OrderItem.objects.create(order=order, product=product, quantity=1)

    messages.success(request, 'Order placed successfully!')
    return redirect('home')

@login_required
def notifications(request):
    # Fetch all orders for the current user
    orders = Order.objects.filter(user=request.user)
    
    # Filter orders based on status and prepare notifications
    pending_orders = orders.filter(status='pending')
    approved_orders = orders.filter(status='confirmed')
    
    return render(request, 'orders/notifications.html', {
        'pending_orders': pending_orders,
        'approved_orders': approved_orders,
    })
