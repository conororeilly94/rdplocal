from django.test import SimpleTestCase
from django.urls import reverse, resolve
from newsletter.views import news_letter, news_emails, news_phones, news_txt_del

class TestUrls(SimpleTestCase):

    def test_newsletter_url_is_resolves(self):
        url = reverse('news_letter')
        self.assertEquals(resolve(url).func, news_letter)


    def test_newsemails_url_is_resolves(self):
        url = reverse('news_emails')
        self.assertEquals(resolve(url).func, news_emails)


    def test_newsphones_url_is_resolves(self):
        url = reverse('news_phones')
        self.assertEquals(resolve(url).func, news_phones)


    def test_newstxtdel_url_is_resolves(self):
        url = reverse('news_txt_del', args=[1, 2])
        self.assertEquals(resolve(url).func, news_txt_del)