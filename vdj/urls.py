from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'groups/([0-9]+)/$', views.group, name='group'),
    url(r'add/$', views.add_lesson, name='add_lesson'),
]