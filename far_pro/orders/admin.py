from django.contrib import admin
from .models import Order, OrderItem

def approve_orders(modeladmin, request, queryset):
    for order in queryset:
        order.status = 'confirmed'
        order.save()
        # Create a notification for the user (if needed)
        # You can add a flash message here if you want to notify the admin
    modeladmin.message_user(request, "Selected orders have been approved.")
approve_orders.short_description = "Approve selected orders"



class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'status', 'created_at']
    actions = [approve_orders]



admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
