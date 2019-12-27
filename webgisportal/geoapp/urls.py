from django.urls import path

from . import views

urlpatterns = [
    path('trees/', views.index, name='index')
]