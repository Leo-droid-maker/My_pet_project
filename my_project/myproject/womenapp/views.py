from django.shortcuts import render, get_object_or_404
from myprojectapp.models import ProductCategory, Product


# Create your views here.

def women(request, pk=None):
    categories_menu = ProductCategory.objects.all().filter(is_active=True)

    if pk is not None:
        if pk == 0:
            women_products = Product.objects.all().filter(gender='female')
            category_item = {'name': 'all', 'pk': 0}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            women_products = Product.objects.filter(
                category=category_item, gender='female')

        content = {
            'title': 'women',
            'categories_menu': categories_menu,
            'women_products': women_products,
            'category_item': category_item,
        }
        return render(request, 'womenapp/women.html', content)

    same_women_products = Product.objects.all().filter(gender='female')
    content = {
        'title': 'women',
        'categories_menu': categories_menu,
        'women_products': same_women_products,
    }
    return render(request, 'womenapp/women.html', content)
