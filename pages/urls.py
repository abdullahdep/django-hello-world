from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('premium', views.premium, name='premium'),
    path('upgrade_premium', views.upgrade_premium, name='upgrade_premium'),
    path('subject', views.subjects, name='subjects'),
    path('subject/<str:subject_name>/', views.subject_detail, name='subject_detail'),
]