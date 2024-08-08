from django.urls import path
from . import views

urlpatterns = [
    path('place_order/<int:product_id>/', views.place_order, name='place_order'),
    path('notifications/', views.notifications, name='notifications'),
]
