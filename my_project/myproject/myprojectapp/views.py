from django.shortcuts import render, get_object_or_404
from myprojectapp.models import PageCategories, ProductCategory, Product, BottomBanners, MainBanner


# Create your views here.

def main(request):
    products = Product.objects.all()[:4]
    bottom_banners = BottomBanners.objects.all()
    main_banner = MainBanner.objects.all()

    content = {
        'title': 'home',
        'products': products,
        'bottom_banners': bottom_banners,
        'main_banner': main_banner
    }

    return render(request, 'myprojectapp/index.html', content)


def about(request):
    content = {
        'title': 'about',
    }
    return render(request, 'myprojectapp/about.html', content)


def page404(request):
    content = {
        'title': '404',
    }
    return render(request, 'myprojectapp/404.html', content)
