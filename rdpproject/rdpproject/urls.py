from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls), # Admin page
    url(r'', include('main.urls')), # Root
    url(r'', include('posts.urls')), # Root
]
