from django.urls import path

from . import views


urlpatterns = [path('', views.index, name='base'), ]        # start adding routes for the app here
