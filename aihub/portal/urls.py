from os import name
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView # new



urlpatterns = [
    path('', views.home, name='index'),
    path('acccounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('search', views.search, name='search')

    # path('add', views.add, name='add')
]
