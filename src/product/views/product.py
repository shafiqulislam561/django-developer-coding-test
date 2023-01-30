from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic import TemplateView

from product.models import Variant, Product, ProductVariant

from product.forms import  ProductForm
from product.filters import ProductFilter


class CreateProductView(generic.TemplateView):
    form_class = ProductForm
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

class ProductView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['product'] = True
        context['variants'] = Variant.objects.all()
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context

class ProductEditView(UpdateView):
    pk_url_kwarg = 'id'