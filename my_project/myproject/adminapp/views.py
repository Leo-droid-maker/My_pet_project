from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from authapp.models import ShopUser
from myprojectapp.models import ProductCategory, Product
from adminapp.forms import ShopUserAdminForm, ProductEditForm, ProductCategoryEditForm
from django.http import HttpResponseRedirect
from authapp.forms import ShopUserRegisterForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:user_read')
    form_class = ShopUserRegisterForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UsersListView(ListView):
    # paginate_by = 1
    model = ShopUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:user_read')
    form_class = ShopUserAdminForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin:user_read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.success_url)

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:category_read')
    # fields = '__all__'
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductCategoryListView(ListView):
    paginate_by = 2
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:category_read')
    # fields = '__all__'
    form_class = ProductCategoryEditForm

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'редактирование категории'
    #     return context
    #
    # def get_success_url(self):
    #     self.object = self.get_object()
    # def get_queryset(self):
    #     return ProductCategory.objects.get(pk=self.kwargs['pk'])

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin:category_read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.success_url)

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    form_class = ProductEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
        context['category'] = category
        return context

    def get_success_url(self):
        return reverse_lazy('admin:products', args=[self.kwargs['pk']])


# class ProductCreateView(CreateView):
#     model = ProductCategory
#     template_name = 'adminapp/product_update.html'
#     form_class = ProductEditForm
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         category_pk = self.get_object().pk
#         context['category'] = category_pk
#         return context
#
#     def get_success_url(self):
#         category_pk = self.get_object().pk
#         # print(f' HERE IS = {category_pk}')
#         return reverse_lazy('admin:products', args=[category_pk])
#
#     @method_decorator(user_passes_test(lambda u: u.is_superuser))
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        return Product.objects.filter(category__pk=category_pk)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
        context['category'] = category
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# class ProductListView(ListView):
#     model = Product
#     template_name = 'adminapp/products.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         category = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
#         products_list = Product.objects.filter(category=category)
#         context['category'] = category
#         context['object_list'] = products_list
#         return context
#
#     @method_decorator(user_passes_test(lambda u: u.is_superuser))
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    form_class = ProductEditForm

    def get_success_url(self):
        category_pk = self.get_object().category.pk
        return reverse_lazy('admin:products', args=[category_pk])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        category = get_object_or_404(ProductCategory, pk=self.object.category.pk)
        context['category'] = category
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# class ProductUpdateView(UpdateView):
#     model = Product
#     template_name = 'adminapp/product_update.html'
#     form_class = ProductEditForm
#
#     # def get_queryset(self):
#     #     return ProductCategory.objects.get(pk=self.kwargs['pk'])
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         category_pk = self.get_object().category.pk
#         context['category'] = category_pk
#         return context
#
#     def get_success_url(self):
#         category_pk = self.get_object().category.pk
#         return reverse_lazy('admin:products', args=[category_pk])
#
#     @method_decorator(user_passes_test(lambda u: u.is_superuser))
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'

    def get_success_url(self):
        category_pk = self.get_object().category.pk
        return reverse_lazy('admin:products', args=[category_pk])

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_detail.html'

    # success_url = reverse_lazy('admin:product_read')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
