from django.urls import path
from . import views

app_name = 'opening'
urlpatterns = [
    path('', views.index, name='index')
]