"""sk_product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from product.views import show_categories, show_category_products, show_product, show_products, last24_products

urlpatterns = [
    url(r'^$', show_categories, name='categories'),
    url(r'^products/$', show_products, name='products'),
    url(r'^last24-products/$', last24_products, name='last24-products'),
    url(r'^products/(?P<category_slug>[\w-]+)/$', show_category_products, name='category_products'),
    url(r'^products/(?P<category_slug>[\w]+)/(?P<product_slug>[\w-]+)/$', show_product, name='product'),
]
