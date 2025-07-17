from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('premium', views.premium, name='premium'),
     path('upgrade_premium', views.upgrade_premium, name='upgrade_premium'),
     path('subject', views.subjects, name='subjects'),
     path('subject/<str:slug>/', views.subject_detail, name='subject_detail'),
     path('subject/<str:subject_slug>/grade/<int:grade>/chapter/<str:chapter_slug>/', 
          views.chapter_detail, name='chapter_detail'),
     path('admin_content_upload', views.admin_content_upload, name='admin_content_upload'),
     path('admin/manage-content/', views.manage_content, name='manage_content'),

     # APIs
     path('api/chapters/<str:subject_slug>/', views.get_chapters, name='get_chapters'),
     path('api/topics/<str:chapter_slug>/', views.get_topics, name='get_topics'),
     path('api/chapters/<str:subject_slug>/<int:grade>/', views.get_grade_chapters, name='get_grade_chapters'),

     # Tests
     path('subject/<str:subject_slug>/grade/<int:grade>/chapter/<str:chapter_slug>/<str:topic>/mcqstest/', 
          views.mcq_test, name='mcq_test'),
     path('subject/<str:subject_slug>/grade/<int:grade>/chapter/<str:chapter_slug>/<str:topic>/shortquestions/', 
          views.short_question_test, name='short_question_test'),

     # Payments
     path('payment/process/', views.generate_jazzcash_form, name='process_payment'),
     path('payment/callback/', views.payment_callback, name='payment_callback'),
     path('payment/jazzcash/ipn/', views.jazzcash_ipn, name='jazzcash_ipn'),

     # Saved content + CRUD
     path('saved-content/', views.saved_content_list, name='saved_content_list'),

     # Optional: Add views.subject_create etc if you use Add buttons in the template
     path('subject/add/', views.subject_create, name='subject_create'),
     path('mcq/add/', views.mcq_create, name='mcq_create'),
     path('shortquestion/add/', views.shortquestion_create, name='shortquestion_create'),
     path('sitemap/', views.html_sitemap, name='html_sitemap'),
         path('mcq/', views.mcq_dashboard, name='mcq_dashboard'),



]
