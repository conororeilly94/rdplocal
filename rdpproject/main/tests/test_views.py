# from django.test import TestCase, Client
# from django.urls import reverse
# from main.models import Main
# from django.contrib.auth.models import User, Group, Permission
# import json

# ###

# class TestViews(TestCase):

#     def setUp(self):
#         self.client = Client
#         self.myregister_url = reverse('myregister')
#         self.myregister1 = User.objects.create_user(
#             name="John",
#             username="johnryan",
#             email="john@gmail.com",
#             pass1="Tghfgdjks94",
#             pass2="Tghfgdjks94"
#         )

#     def test_myregister_list_POST(self):

#         response = self.client.post(self.myregister1, {
#             'name':'John',
#             'username':'johnryan',
#             'email':'john@gmail.com',
#             'pass1':'Tghfgdjks94',
#             'pass2':'Tghfgdjks94'
#         })

#         self.assertEquals(response.status_code, 302)
#         self.assertEquals(self.myregister1.name, 'John')