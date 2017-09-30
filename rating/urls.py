from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<username>\w+)/$', views.get_user, name = 'get-user'),
]