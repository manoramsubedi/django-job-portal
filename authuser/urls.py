from django.urls import path
from authuser import views

urlpatterns = [
    path('candidate-register/', views.register_candidate, name='candidate_register'),
    path('hr-register/', views.register_hr, name='hr_register'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
]
