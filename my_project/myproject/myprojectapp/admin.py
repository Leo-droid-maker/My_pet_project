from django.contrib import admin
from myprojectapp.models import PageCategories, ProductCategory, Product, BottomBanners
from cartapp.models import Cart

# Register your models here.

admin.site.register(PageCategories)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(BottomBanners)
admin.site.register(Cart)

