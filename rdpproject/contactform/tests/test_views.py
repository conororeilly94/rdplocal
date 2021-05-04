from django.test import TestCase, Client
from django.urls import reverse
from contactform.models import ContactForm
from django.contrib.auth.models import User, Group, Permission
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.contact_url = reverse('contact_add')
        self.contactshow_url = reverse('contact_show')
        self.contactdel_url = reverse('contact_del', args=[1])
        self.contactform1 = ContactForm.objects.create(
            name="Ryan",
            email="ryan@gmail.com",
            text="Hello",
            time=1,
            date=1
        )


    def test_contactformadd_POST(self):

        response = self.client.post(self.contact_url, {
            'name':'Ryan',
            'email':'ryan@gmail.com',
            'text':'Hello',
            'time':1,
            'date':1
        })

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.contactform1.name, 'Ryan')



    def test_contactformdel_DELETE(self):
    
        ContactForm.objects.create(
            name="Ryan",
            email="ryan@gmail.com",
            text="Hello",
            time=1,
            date=1
        )

        response = self.client.delete(self.contactdel_url, json.dumps({
            'name':'Ryan',
            'email':'ryan@gmail.com',
            'text':'Hello',
            'time':1,
            'date':1
        }))

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.contactform1.name, 'Ryan')