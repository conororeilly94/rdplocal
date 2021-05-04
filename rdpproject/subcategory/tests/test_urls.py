from django.test import SimpleTestCase
from django.urls import reverse, resolve
from subcategory.views import subcat_list, subcat_add, subcat_del

class TestUrls(SimpleTestCase):

    def test_subcatlist_url_is_resolves(self):
        url = reverse('subcat_list')
        self.assertEquals(resolve(url).func, subcat_list)


    def test_subcatadd_url_is_resolves(self):
        url = reverse('subcat_add')
        self.assertEquals(resolve(url).func, subcat_add)


    def test_subcatdel_url_is_resolves(self):
        url = reverse('subcat_del', args=[1])
        self.assertEquals(resolve(url).func, subcat_del)