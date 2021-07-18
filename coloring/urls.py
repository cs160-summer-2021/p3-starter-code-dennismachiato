from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('home', views.home, name='home'),
    path('new_interaction', views.index, name='new_interaction')
]
