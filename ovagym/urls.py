from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('classes/', views.classes, name='classes'),
    path('single/', views.single, name='single'),
    path('feature/', views.feature, name='feature'),
    
]