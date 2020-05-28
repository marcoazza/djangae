from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    url(r'^start$', views.start),
    url(r'^stop$', views.stop),
    url(r'^warmup$', views.warmup),
    url(r'^clearsessions$', views.clearsessions),
    path('', include('djangae.tasks.urls')),
]
