from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('output', views.output, name = "output"),
    path('request', views.request, name = "request"),
    path('all', views.all, name = "all")
]

