# pylint: disable=import-error
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)

from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})

    if not bag:
            messages.error(request,
                           "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Oe1qBL7H8GMiIX4bVsKyZRwdghG9byXaSF7JubTnFxqRoJCN38hAiCfW8mxTJLg0V3ivEd1iaV6CbeRVmssIBQ800uww5vMOb',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)