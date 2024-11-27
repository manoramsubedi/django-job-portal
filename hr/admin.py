from django.contrib import admin

from hr.models import Hr, JobPost, CandidateApplication, SelectCandidate

# Register your models here.
class HrAdmin(admin.ModelAdmin):
    list_display=('id', 'user')
admin.site.register(Hr, HrAdmin)

class JobPostAdmin(admin.ModelAdmin):
    list_display=('id', 'user', 'title', 'apply_count', 'last_date')
admin.site.register(JobPost, JobPostAdmin)

class CandidateApplicationAdmin(admin.ModelAdmin):
    list_display=('id', 'user', 'job', 'experience', 'status')
admin.site.register(CandidateApplication, CandidateApplicationAdmin)

class SelectCandidateAdmin(admin.ModelAdmin):
    list_display=('id', 'job', 'candidate')
admin.site.register(SelectCandidate, SelectCandidateAdmin)
