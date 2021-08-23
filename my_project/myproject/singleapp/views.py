from django.shortcuts import render, get_object_or_404
from myprojectapp.models import ProductCategory, Product


def single(request, pk):
    categories_menu = ProductCategory.objects.all()
    product = get_object_or_404(Product, pk=pk)

    related_products = Product.objects.filter(
        gender=product.gender).exclude(pk=product.pk).order_by('?')[:3]

    content = {
        'title': 'single',
        'product': product,
        'categories_menu': categories_menu,
        'related_products': related_products
    }
    return render(request, 'singleapp/single.html', content)
