from django.urls import path
from candidate import views

urlpatterns = [
    path('candidate-dashboard', views.candidate_dashboard, name='candidate_dashboard')
]
