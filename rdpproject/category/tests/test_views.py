from django.test import TestCase, Client
from django.urls import reverse
from category.models import Category
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.catadd_url = reverse('cat_add')
        self.catdel_url = reverse('cat_del', args=[1])
        self.category1 = Category.objects.create(
            name="Pica"
        )

    def test_catadd_POST(self):

        response = self.client.post(self.catadd_url, {
            'name': 'Pica',
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.category1.name, 'Pica')


    def test_catdel_DELETE(self):

        Category.objects.create(
            name="Pica"
        )

        response = self.client.delete(self.catdel_url, json.dumps({
            'name': 'Pica'
        }))

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.category1.name, 'Pica')