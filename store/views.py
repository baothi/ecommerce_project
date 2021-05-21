from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product
# Create your views here.

def home(request, category_slug=None):
  category_page = None
  products = None
  if category_slug != None:
    category_page = get_object_or_404(Category,slug=category_slug)
    products = Product.objects.filter(category=category_page,available=True)
  else:
    products = Product.objects.all().filter(available=True)
  # breakpoint()
  return render(request, 'home.html',{
    'category': category_page,
    'products': products
    })

def productPage(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    # if request.method == 'POST' and request.user.is_authenticated and request.POST['content'].strip() != '':
    #     Review.objects.create(product=product,
    #                           user=request.user,
    #                           content=request.POST['content'])

    # reviews = Review.objects.filter(product=product)

    return render(request, 'product.html', {'product': product})
