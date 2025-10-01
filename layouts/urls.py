from django.urls import path 
from . import views


urlpatterns = [
    path('layouts/', views.layouts, name='layouts'),
    path('home/', views.home, name='home'),
    path('subjects/', views.subjects, name='subjects'),
    path('premium/', views.premium, name='premium'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('subject_detail/', views.subject_detail, name='subject_detail'),
    path('privacy-policy', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions', views.terms_and_conditions, name='terms_and_conditions'),
    path("ads.txt", views.ads_txt, name="ads_txt"),

    
]