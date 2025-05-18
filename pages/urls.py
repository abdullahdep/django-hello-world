from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('premium', views.premium, name='premium'),
    path('upgrade_premium', views.upgrade_premium, name='upgrade_premium'),
    path('subject', views.subjects, name='subjects'),
    path('subject/<str:slug>/', views.subject_detail, name='subject_detail'),
    path('subject/<str:subject_slug>/chapter/<str:chapter_slug>/', 
         views.chapter_detail, name='chapter_detail'),
]