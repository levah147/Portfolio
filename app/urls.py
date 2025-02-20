from django. urls import path
from . import views

app_name = "app"
urlpatterns = [
     path('', views.index, name='index'),
     # path('about/', views.about, name='about'),
     # path('contact/', views.contact, name='contact'),
     # path('teams/', views.teams, name='teams'),
     # path('services/', views.services, name='services'),
     path('skill/', views.skill, name='skills'),
     path('contact/', views.contact, name='contact'),
     # path('hire/', views.hire, name='hire'),

]
