from django.test import TestCase, Client
from django.urls import reverse
from comment.models import Comment
from posts.models import Posts
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.postscmadd_url = reverse('posts_cm_add', args=[1])
        self.commentdel_url = reverse('comments_del', args=[2])
        self.comment1 = Comment.objects.create(
            name="Ryan",
            email="email@email.com",
            cm='Comment',
            posts_id=1,
            date=1,
            time=1
        )


    def test_commentadd_POST(self):
    
        response = self.client.post(self.postscmadd_url, {
            'name': "Ryan",
            'email': "email@email.com",
            'cm': 'Comment',
            'posts_id': 1,
            'date':1,
            'time':1
        })

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.comment1.name, 'Ryan')


    def test_commentdel_DELETE(self):
        
        Comment.objects.create(
            name="Ryan",
            email="email@email.com",
            cm="Comment",
            posts_id=1,
            date=1,
            time=1
        )

        response = self.client.delete(self.commentdel_url, json.dumps({
            'name': "Ryan",
            'email': "email@email.com",
            'cm': 'Comment',
            'posts_id': 1,
            'date': 1,
            'time': 1
        }))

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.comment1.name, 'Ryan')


    