from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hr(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class JobPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    salary_low = models.IntegerField(default=0)
    salary_high= models.IntegerField(default=0)
    apply_count = models.IntegerField(default=0)
    last_date = models.DateField()

    def __str__(self):
        return self.title

STATUS_CHOICES = {
    ('pending','pending'),
    ('selected','selected')
}

class CandidateApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    pass_year = models.IntegerField()
    experience = models.IntegerField(default=0)
    resume = models.FileField(upload_to='resume')
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='pending')

class SelectCandidate(models.Model):
    job =models.ForeignKey(JobPost, on_delete=models.CASCADE)
    candidate = models.OneToOneField(CandidateApplication, on_delete=models.CASCADE)
