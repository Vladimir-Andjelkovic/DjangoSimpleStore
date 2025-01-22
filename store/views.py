from django.shortcuts import render
from djangostore.constants import HOMEPAGE_TEMPLATE
from products.models import Product


def homepage_view(request):
    featured_products = Product.objects.filter(featured=True)

    return render(
        request,
        HOMEPAGE_TEMPLATE,
        {'featured_products': featured_products}
    )
