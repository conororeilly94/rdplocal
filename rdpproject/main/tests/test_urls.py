from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import about, home, panel, mylogin, mylogout, site_setting, about_setting, contact, change_pass, myregister, answer_contactform

class TestUrls(SimpleTestCase):

    def test_about_url_is_resolves(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)


    def test_home_url_is_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    
    def test_panel_url_is_resolves(self):
        url = reverse('panel')
        self.assertEquals(resolve(url).func, panel)

    
    def test_login_url_is_resolves(self):
        url = reverse('mylogin')
        self.assertEquals(resolve(url).func, mylogin)


    def test_logout_url_is_resolves(self):
        url = reverse('mylogout')
        self.assertEquals(resolve(url).func, mylogout)


    def test_sitesetting_url_is_resolves(self):
        url = reverse('site_setting')
        self.assertEquals(resolve(url).func, site_setting)


    def test_aboutsetting_url_is_resolves(self):
        url = reverse('about_setting')
        self.assertEquals(resolve(url).func, about_setting)


    def test_contact_url_is_resolves(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)


    def test_changepass_url_is_resolves(self):
        url = reverse('change_pass')
        self.assertEquals(resolve(url).func, change_pass)


    def test_myregister_url_is_resolves(self):
        url = reverse('myregister')
        self.assertEquals(resolve(url).func, myregister)


    def test_answercontact_url_is_resolves(self):
        url = reverse('answer_contactform', args=[2])
        self.assertEquals(resolve(url).func, answer_contactform)
    
