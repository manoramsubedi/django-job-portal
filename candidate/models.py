from django.db import models
from django.contrib.auth.models import User
from hr.models import CandidateApplication, JobPost
# Create your models here.


class MyJobList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.OneToOneField(CandidateApplication, on_delete=models.CASCADE)
    applied_date = models.DateField(auto_now_add=True)

class IsSortList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.OneToOneField(JobPost, on_delete=models.CASCADE)
    applied_date = models.DateField(auto_now_add=True)
