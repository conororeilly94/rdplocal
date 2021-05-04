from django.test import TestCase, Client
from django.urls import reverse
from subcategory.models import SubCategory
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.subcatadd_url = reverse('subcat_add')
        self.subcatdel_url = reverse('subcat_del', args=[1])
        self.subcategory1 = SubCategory.objects.create(
            name="Tips",
            catname="Pica",
            catid=2
        )

    def test_subcatadd_POST(self):

        response = self.client.post(self.subcatadd_url, {
            'name': 'Tips',
            'catname': 'Pica',
            'catid': 2
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.subcategory1.name, 'Tips')
        # self.assertEquals(self.category1.name, 'Moebius Syndrome')


    def test_subcatdel_DELETE(self):
    
        SubCategory.objects.create(
            name="Tips",
            catname="Pica",
            catid=2
        )

        response = self.client.delete(self.subcatdel_url, json.dumps({
            'name': 'Tips',
            'catname': 'Pica',
            'catid': 2
        }))

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.subcategory1.name, 'Tips')