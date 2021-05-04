from django.test import TestCase, Client
from django.urls import reverse
from newsletter.models import Newsletter
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.newsletter_url = reverse('news_letter')
        self.newsletter_url = reverse('news_letter')
        self.newsletter1 = Newsletter.objects.create(
            txt="Text",
            status=1
        )

    def test_subcatadd_POST(self):

        response = self.client.post(self.newsletter_url, {
            'txt': "Text",
            'status': 1
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.newsletter1.txt, 'Text')

