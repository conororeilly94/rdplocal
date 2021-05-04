from django.test import TestCase, Client
from django.urls import reverse
from manager.models import Manager
from django.contrib.auth.models import User, Group, Permission
import json

####
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.managerlist_url = reverse('manager_list')
        self.managerdel_url = reverse('manager_del', args=[1])
        self.managergroupadd_url = reverse('manager_group_add')
        # self.user = User.objects.create_user('John', 'john', 'john@gmail.com', 'Tghfgdjks94!', 'Tghfgdjks94!')
        self.manager1 = Manager.objects.create(
            name="Ryan",
            utxt="Text",
            email="email@email.com",
        )


    def test_managerlist_GET(self):
        # self.client.login(uname='john', pass1='Tghfgdjks94!')
        response = self.client.get(self.managerlist_url)

        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'main/manager_list.html')


    def test_managergroupadd_POST(self):
    
        response = self.client.post(self.managergroupadd_url, {
            'name': 'Ryan',
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.manager1.name, 'Ryan')


    def test_managerdel_DELETE(self):
        
        Manager.objects.create(
            name="Ryan",
            utxt="Text",
            email="email@email.com",
        )

        response = self.client.delete(self.managerdel_url, json.dumps({
            'name': "Ryan",
            'utxt': "Text",
            'email': "email@email.com",
        }))

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.manager1.name, 'Ryan')