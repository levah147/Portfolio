from django. urls import path
from . import views
from .views import download_cv



app_name = "app"
urlpatterns = [
     path('', views.index, name='index'),
     path('download-cv/', download_cv, name='download_cv'),
     path('contact/', views.contact_view, name='contact'),
     
     # path('about/', views.about, name='about'),
     # path('contact/', views.contact, name='contact'),
     # path('teams/', views.teams, name='teams'),
     # path('services/', views.services, name='services'),
     path('skill/', views.skill, name='skills'),
     # path('hire/', views.hire, name='hire'),

]
