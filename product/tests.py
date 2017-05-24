from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Category
from django.test.client import Client


# django_test_manage.py test product --settings=test_settings

class testShowCategoryProducts(TestCase):
    def setUp(self):
        Category.objects.create(name="car", slug="car", description='This is a category cars')
        Category.objects.create(name="moto", slug="moto", description='This is a category moto')
        Category.objects.create(name="bycicle", slug="bycicle", description='This is a category bycicle')

    def test_normal(self):
        c = Client()
        categories = Category.objects.all()

        for category in categories:
            code = c.get(reverse('category_products', args=[category.name])).status_code
            self.assertEqual(code, 200)

    def test_404(self):
        c = Client()
        categories = Category.objects.all()

        for category in categories:
            code = c.get(reverse('category_products', args=[category.name * 2])).status_code
            self.assertEqual(code, 404)
