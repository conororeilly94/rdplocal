from django.test import SimpleTestCase
from django.urls import reverse, resolve
from category.views import cat_list, cat_add, cat_del

class TestUrls(SimpleTestCase):

    def test_catlist_url_is_resolves(self):
        url = reverse('cat_list')
        self.assertEquals(resolve(url).func, cat_list)


    def test_catadd_url_is_resolves(self):
        url = reverse('cat_add')
        self.assertEquals(resolve(url).func, cat_add)


    def test_catdel_url_is_resolves(self):
        url = reverse('cat_del', args=[1])
        self.assertEquals(resolve(url).func, cat_del)