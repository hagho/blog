from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^/(?P<my_args>\d+)/$', views.detail, name='detail'),
    url(r'^test/$', views.test),
]
