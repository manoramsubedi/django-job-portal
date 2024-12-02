from django.urls import path
from hr import views

urlpatterns = [
    path('hrdashboard/', views.HrHome, name='hrdash'),
    path('job-post/', views.post_job, name='postjob'),
    path('candidate-details/<int:pk>/', views.candidate_detail, name='candidate_details'),
    path('select-candidate', views.select_candidate, name='select_candidate'),
    path('reject-candidate', views.reject_candidate, name='reject_candidate'),
]
