from django.test import SimpleTestCase
from django.urls import reverse, resolve
from posts.views import posts_list, posts_add, all_posts, all_posts_search, posts_detail, posts_delete, posts_edit, posts_publish

class TestUrls(SimpleTestCase):

    def test_postlist_url_is_resolves(self):
        url = reverse('posts_list')
        self.assertEquals(resolve(url).func, posts_list)

        
    def test_postadd_url_is_resolves(self):
        url = reverse('posts_add')
        self.assertEquals(resolve(url).func, posts_add)


    def test_allposts_url_is_resolves(self):
        url = reverse('all_posts')
        self.assertEquals(resolve(url).func, all_posts)


    def test_allpostssearch_url_is_resolves(self):
        url = reverse('all_posts_search')
        self.assertEquals(resolve(url).func, all_posts_search)


    def test_postdetail_url_is_resolves(self):
        url = reverse('posts_detail', args=['some-text'])
        self.assertEquals(resolve(url).func, posts_detail)

    
    def test_postdetail_url_is_resolves(self):
        url = reverse('posts_detail', args=['some-text'])
        self.assertEquals(resolve(url).func, posts_detail)


    def test_postdelete_url_is_resolves(self):
        url = reverse('posts_delete', args=[1])
        self.assertEquals(resolve(url).func, posts_delete)


    def test_postedit_url_is_resolves(self):
        url = reverse('posts_edit', args=[1])
        self.assertEquals(resolve(url).func, posts_edit)


    def test_postpublish_url_is_resolves(self):
        url = reverse('posts_publish', args=[1])
        self.assertEquals(resolve(url).func, posts_publish)