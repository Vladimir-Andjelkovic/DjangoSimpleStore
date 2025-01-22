from django.shortcuts import render, redirect, get_object_or_404
from cart.models import CartItem, Cart
from djangostore import constants
from .models import Order


def checkout_view(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.total_price() for item in cart_items)
    user = request.user if request.user.is_authenticated else None

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']

        order = Order.objects.create(
            name=name,
            email=email,
            address=address,
            total_price=total_price,
            user=user,
            cart=cart
        )

        order.save_order_items()
        cart_items.delete()

        return redirect(constants.ORDER_CONFIRMATION_URL, order_id=order.id)

    return render(
        request=request,
        template_name=constants.CHECKOUT_TEMPLATE,
        context={'cart_items': cart_items, 'total_price': total_price}
    )


def order_confirmation_view(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(
        request=request,
        template_name=constants.ORDER_CONFIRMATION_TEMPLATE,
        context={'order': order}
    )
