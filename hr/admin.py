from django.contrib import admin

from hr.models import Hr, JobPost, CandidateApplication, SelectCandidate

# Register your models here.

admin.site.register(Hr)
admin.site.register(JobPost)
admin.site.register(CandidateApplication)
admin.site.register(SelectCandidate)
