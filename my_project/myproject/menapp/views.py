from django.shortcuts import render, get_object_or_404
from myprojectapp.models import ProductCategory, Product
# from django.views.generic.base import TemplateView
# from django.urls import reverse_lazy

# Create your views here.


# class Men_view(TemplateView):
#     template_name = 'menapp/men.html'

#     def get_success_url(self):
#         return reverse_lazy('men:men_category', args=[self.kwargs['pk']])

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'men'
#         context['categories_menu'] = ProductCategory.objects.all().filter(
#             is_active=True)
#         pk = self.kwargs['pk']
#         pk = None
#         if pk is not None:
#             if pk == 0:
#                 context['men_products'] = Product.objects.all().filter(
#                     gender='male')
#                 context['category_item'] = {'name': 'all', 'pk': 0}
#             else:
#                 context['category_item'] = get_object_or_404(
#                     ProductCategory, pk=pk)
#                 context['men_products'] = Product.objects.filter(
#                     category=context['category_item'], gender='male')
#         context['men_products'] = Product.objects.all().filter(gender='male')
#         return context


def men(request, pk=None):
    categories_menu = ProductCategory.objects.all().filter(is_active=True)

    if pk is not None:
        if pk == 0:
            men_products = Product.objects.all().filter(gender='male')
            category_item = {'name': 'all', 'pk': 0}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            men_products = Product.objects.filter(
                category=category_item, gender='male')

        content = {
            'title': 'men',
            'categories_menu': categories_menu,
            'men_products': men_products,
            'category_item': category_item,
        }
        return render(request, 'menapp/men.html', content)

    same_men_products = Product.objects.all().filter(gender='male')
    content = {
        'title': 'men',
        'categories_menu': categories_menu,
        'men_products': same_men_products,
    }
    return render(request, 'menapp/men.html', content)
