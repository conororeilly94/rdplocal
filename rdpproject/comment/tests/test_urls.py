from django.test import SimpleTestCase
from django.urls import reverse, resolve
from comment.views import posts_cm_add, comments_list, comments_del, comments_confirm

class TestUrls(SimpleTestCase):

    def test_postscmadd_url_is_resolves(self):
        url = reverse('posts_cm_add', args=[1])
        self.assertEquals(resolve(url).func, posts_cm_add)


    def test_cmlist_url_is_resolves(self):
        url = reverse('comments_list')
        self.assertEquals(resolve(url).func, comments_list)


    def test_cmdel_url_is_resolves(self):
        url = reverse('comments_del', args=[1])
        self.assertEquals(resolve(url).func, comments_del)


    def test_cmconfirm_url_is_resolves(self):
        url = reverse('comments_confirm', args=[1])
        self.assertEquals(resolve(url).func, comments_confirm)