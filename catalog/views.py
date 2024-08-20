from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_dict = {}
        for product in Product.objects.all():
            for version in Version.objects.all():
                if version.indicates_current_version:
                    if version.product_id == int(product.pk):
                        version_dict[version.product_id] = version.version_name
        context_data['versions'] = version_dict
        return context_data


class ProductDetailView(DetailView):
    model = Product


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Product.objects.all()[:5]
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.author = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.author:
            return ProductForm
        if user.has_perm('catalog.can_edit_product_description') and user.has_perm(
                'catalog.can_edit_product_category') and user.has_perm('catalog.can_cancel_publication'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.author:
            return ProductForm
        raise PermissionDenied
