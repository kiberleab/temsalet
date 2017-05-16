from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^menu/$', views.menu_list, name='menu_list'),
    url(r'^news-event/$', views.newsevent_list, name='newsevent_list'),
    url(r'^our-story/$', views.our_story, name='our_story'),
    url(r'^community/$', views.community, name='community'),
]