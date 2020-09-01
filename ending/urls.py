from django.urls import path
from . import views

app_name = 'ending'
urlpatterns = [
    path('', views.index, name='index')
]