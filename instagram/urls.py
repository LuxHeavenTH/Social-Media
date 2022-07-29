from django.urls import path #importing the necessary documents

from . import views

app_name ='instagram'

urlpatterns = [
  path('', views.index, name='index'),
]