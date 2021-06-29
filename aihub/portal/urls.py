from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='index'),
    path('add', views.add, name='add')
]


# urlpatterns = ...

urlpatterns += staticfiles_urlpatterns()