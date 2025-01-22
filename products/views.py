from django.shortcuts import render, get_object_or_404
from .models import Product
from djangostore.constants import PRODUCT_DISPLAY_PAGE_TEMPLATE


def pdp_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(
        request,
        PRODUCT_DISPLAY_PAGE_TEMPLATE,
        {'product': product}
    )
