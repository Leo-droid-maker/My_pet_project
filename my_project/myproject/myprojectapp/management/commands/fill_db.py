import json
import os
from django.conf import settings
from authapp.models import ShopUser
from myprojectapp.models import ProductCategory, BottomBanners, Product, MainBanner
from django.core.management import BaseCommand


def load_from_json(file_name):
    with open(os.path.join(settings.BASE_DIR, f'myprojectapp/json/{file_name}.json'), 'r', encoding='utf-8') as f:
        return json.load(f)


class Command(BaseCommand):

    def handle(self, *args, **options):

        # categories = load_from_json('categories')
        # ProductCategory.objects.all().delete()
        # for category in categories:
        #     ProductCategory.objects.create(**category)

        # bottom_banners = load_from_json('products_for_bottom_banner')
        # BottomBanners.objects.all().delete()
        # for banner in bottom_banners:
        #     _category = ProductCategory.objects.get(name=banner['category'])
        #     banner['category'] = _category
        #     BottomBanners.objects.create(**banner)

        # products = load_from_json('products')
        # Product.objects.all().delete()
        # for product in products:
        #     _category = ProductCategory.objects.get(name=product['category'])
        #     product['category'] = _category
        #     Product.objects.create(**product)

        main_banner = load_from_json('images_for_main_banner')
        MainBanner.objects.all().delete()
        for banner in main_banner:
            MainBanner.objects.create(**banner)

        # ShopUser.objects.create_superuser(
        #     'django', 'django@local.gb', 'geekbrains', age=34)
