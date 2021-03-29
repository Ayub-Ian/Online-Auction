from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Product
from .forms import BidsForm


# Create your views here.

class HomeView(View):
    template_name = 'auction/index.html'
    model = Product

    def get(self, request, *args, **kwargs):
        context = {'product_list': Product.objects.all()}
        return render(request, self.template_name, context)


class AboutView(View):
    template_name = 'auction/about.html'

    def get(self, request):
        return render(request, self.template_name)


class ProductView(View):
    template_name = 'auction/product_detail.html'

    def get(self, request, id, *args, **kwargs):
        product = Product.objects.get(id=id)
        context = {'name': product.name, 'description': product.description, 'image': product.image}
        return render(request, self.template_name, context)

