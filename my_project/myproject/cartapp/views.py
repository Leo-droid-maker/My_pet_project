from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from cartapp.models import Cart
from django.contrib.auth.decorators import login_required

from myprojectapp.models import Product


@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user).order_by('product__category')

    content = {
        'title': 'cart',
        'cart_items': cart_items
    }
    return render(request, 'cartapp/cart.html', content)


@login_required
def cart_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('single:product', args=[pk]))

    product_item = get_object_or_404(Product, pk=pk)
    cart_item = Cart.objects.filter(product=product_item, user=request.user).first()

    if not cart_item:
        cart_item = Cart(user=request.user, product=product_item)

    cart_item.quantity += 1
    cart_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def cart_remove(request, pk):
    cart_item = get_object_or_404(Cart, pk=pk)
    cart_item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def cart_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_cart_item = Cart.objects.get(pk=pk)

        if quantity > 0:
            new_cart_item.quantity = quantity
            new_cart_item.save()
        else:
            new_cart_item.delete()

        cart_items = Cart.objects.filter(user=request.user).order_by('product__category')

        content = {
            'cart_items': cart_items
        }

        result = render_to_string('cartapp/includes/inc_cart_list.html', content)

        return JsonResponse({'result': result})
