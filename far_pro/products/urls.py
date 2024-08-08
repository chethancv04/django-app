from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('my_products/', views.product_list, name='product_list'),

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),

    path('seller_dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),

]