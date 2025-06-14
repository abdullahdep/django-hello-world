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
    path('admin_content_upload', views.admin_content_upload, name='admin_content_upload'),
    path('api/chapters/<str:subject_slug>/', views.get_chapters, name='get_chapters'),
    path('api/topics/<str:chapter_slug>/', views.get_topics, name='get_topics'),
    path('api/chapters/<str:subject_slug>/<int:grade>/', views.get_grade_chapters, name='get_grade_chapters'),
    path('test/<int:test_id>/', views.test_view, name='test_view'),
    path('test/<int:test_id>/review/', views.test_review, name='test_review'),
    path('test/<str:topic_slug>/mcq/', views.mcq_test_view, name='mcq_test'),
    path('test/<str:topic_slug>/short/', views.short_test_view, name='short_test'),
    path('sitemap/', views.html_sitemap, name='html_sitemap'),
]