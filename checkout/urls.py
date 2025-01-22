from django.urls import path
from djangostore.constants import CHECKOUT_URL, ORDER_CONFIRMATION_URL
from . import views


urlpatterns = [
    path('<int:cart_id>/', views.checkout_view, name=CHECKOUT_URL),
    path('order-confirmation/<int:order_id>/', views.order_confirmation_view, name=ORDER_CONFIRMATION_URL)
]
