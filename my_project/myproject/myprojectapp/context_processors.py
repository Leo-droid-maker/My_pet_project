from cartapp.models import Cart


def cart(request):
    cart_list = []
    if request.user.is_authenticated:
        cart_list = Cart.objects.filter(user=request.user)
    return {
        'cart': cart_list
    }
