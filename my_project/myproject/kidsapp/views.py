from django.shortcuts import render, get_object_or_404
from myprojectapp.models import ProductCategory, Product


# Create your views here.

def kids(request, pk=None):
    categories_menu = ProductCategory.objects.all().filter(is_active=True)

    if pk is not None:
        if pk == 0:
            kids_products = Product.objects.all().filter(gender='kids')
            category_item = {'name': 'all', 'pk': 0}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            kids_products = Product.objects.filter(
                category=category_item, gender='kids')

        content = {
            'title': 'kids',
            'categories_menu': categories_menu,
            'kids_products': kids_products,
            'category_item': category_item,
        }
        return render(request, 'kidsapp/kids.html', content)

    same_kids_products = Product.objects.all().filter(gender='kids')
    content = {
        'title': 'kids',
        'categories_menu': categories_menu,
        'kids_products': same_kids_products,
    }
    return render(request, 'kidsapp/kids.html', content)
