from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^posts/(?P<word>.*)/$', views.posts_detail, name='posts_detail'),
    url(r'^panel/posts/list/$', views.posts_list, name='posts_list'),
    url(r'^panel/posts/add/$', views.posts_add, name='posts_add'),
    url(r'^panel/posts/del/(?P<pk>\d+)$', views.posts_delete, name='posts_delete'),
    url(r'^panel/posts/edit/(?P<pk>\d+)$', views.posts_edit, name='posts_edit'),

]