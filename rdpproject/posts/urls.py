from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^posts/(?P<word>.*)/$', views.posts_detail, name='posts_detail'),
]