from django.test import SimpleTestCase
from django.urls import reverse, resolve
from contactform.views import contact_add, contact_show, contact_del

class TestUrls(SimpleTestCase):

    def test_postscmadd_url_is_resolves(self):
        url = reverse('contact_add')
        self.assertEquals(resolve(url).func, contact_add)


    def test_cmlist_url_is_resolves(self):
        url = reverse('contact_show')
        self.assertEquals(resolve(url).func, contact_show)


    def test_cmdel_url_is_resolves(self):
        url = reverse('contact_del', args=[1])
        self.assertEquals(resolve(url).func, contact_del)
