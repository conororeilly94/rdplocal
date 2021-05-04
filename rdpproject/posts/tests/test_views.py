from django.test import TestCase, Client
from django.urls import reverse
from posts.models import Posts
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.posts_url = reverse('posts_add')
        self.postdel_url = reverse('posts_delete', args=[1])
        self.posts1 = Posts.objects.create(
            name="Name",
            short_txt="Short txt",
            body_txt="Long txt",
            date=1,
            time=1,
            img="Image",
            imgurl="Img Url",
            author="Author",
            catname="Category",
            catid=1,
            ocatid=1,
            views=1,
            tag='Tag',
            act=1,
            rand=1
        )

    def test_postadd_POST(self):

        response = self.client.post(self.posts_url, {
            'name': "Name",
            'short_txt': "Short txt",
            'body_txt': "Long txt",
            'date': 1,
            'time': 1,
            'img': "Image",
            'imgurl': "Img Url",
            'author': "Author",
            'catname': "Category",
            'catid': 1,
            'ocatid': 1,
            'views': 1,
            'tag': 'Tag',
            'act': 1,
            'rand':1
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.posts1.name, 'Name')


    def test_postdel_DELETE(self):
    
        Posts.objects.create(
            name="Name",
            short_txt="Short txt",
            body_txt="Long txt",
            date=1,
            time=1,
            img="Image",
            imgurl="Img Url",
            author="Author",
            catname="Category",
            catid=1,
            ocatid=1,
            views=1,
            tag='Tag',
            act=1,
            rand=1
        )

        response = self.client.delete(self.postdel_url, json.dumps({
            'name': "Name",
            'short_txt': "Short txt",
            'body_txt': "Long txt",
            'date': 1,
            'time': 1,
            'img': "Image",
            'imgurl': "Img Url",
            'author': "Author",
            'catname': "Category",
            'catid': 1,
            'ocatid': 1,
            'views': 1,
            'tag': 'Tag',
            'act': 1,
            'rand':1
        }))

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.posts1.name, 'Name')