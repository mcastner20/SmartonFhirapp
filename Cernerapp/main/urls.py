from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('intro/', views.questions, name='questions'),
    path('disaster/', views.disaster, name='disaster'),
    path('demographic/', views.demographic, name='demographic'),
    path('hazard2/', views.hazard2, name='hazard2'),
    path('hazard_continued/', views.hazard_continued, name='hazard_continued'),
    path('hazard_probability/', views.hazard_probability, name='hazard_probability'),
    path('results/', views.results, name='results')
    ]