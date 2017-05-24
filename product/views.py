from datetime import date
from django.shortcuts import render, get_object_or_404

# Create your views here.
from product.models import Category, Product
from sk_product.settings import STATIC_ROOT


def show_categories(request):
    msg = 'Categories'
    print(STATIC_ROOT)
    categories = Category.objects.all()

    context = {
        'msg': msg,
        'categories': categories,
    }
    return render(request, 'product/categories.html', context)


def show_products(request):
    msg = 'Products'
    products = Product.objects.all()

    context = {
        'msg': msg,
        'products': products,
    }
    return render(request, 'product/products.html', context)


def show_category_products(request, category_slug=None):
    msg = 'Category products'
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.all().filter(category=category.id).order_by('id')

    context = {
        'msg': msg,
        'category': category,
        'products': products,
    }
    return render(request, 'product/products_category.html', context)


def show_product(request, category_slug=None, product_slug=None):
    msg = 'Product'
    category = get_object_or_404(Category, slug=category_slug)
    product = Product.objects.get(slug=product_slug, category__slug=category_slug)

    context = {
        'msg': msg,
        'category': category,
        'product': product,
    }
    return render(request, 'product/product.html', context)


def last24_products(request):
    if request.user.is_authenticated():
        msg = 'Last 24h products'
        last_products = Product.objects.all().filter(created_at__day__gte=date.today().day - 1)
        context = {
            'msg': msg,
            'products': last_products
        }

        return render(request, 'product/last24-products.html', context)
    else:
        msg = 'The page is available for registered users'
        context = {
            'msg': msg
        }
        return render(request, 'product/last24-products.html', context)
