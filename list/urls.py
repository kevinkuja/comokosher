from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<shop>/', views.detail, name='detail'),

]