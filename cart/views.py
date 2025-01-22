from django.shortcuts import render, get_object_or_404, redirect
from djangostore.constants import CART_TEMPLATE, CART_URL
from products.models import Product
from .models import Cart, CartItem


def cart_view(request):
    cart = get_cart(request)

    return render(
        request,
        CART_TEMPLATE,
        {'cart': cart}
    )


def get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_id = request.session.session_key
        if not session_id:
            request.session.create()
            session_id = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_id=session_id)

    return cart


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_cart(request)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect(CART_URL)
