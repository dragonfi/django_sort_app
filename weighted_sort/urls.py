from django.conf.urls import patterns, url

from weighted_sort import views

urlpatterns = patterns('',
    url(r'^$', views.weighted_sort, name='weighted_sort'),
)
