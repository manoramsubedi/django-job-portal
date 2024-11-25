from django.contrib import admin
from candidate.models import MyJobList, IsSortList
# Register your models here.

class MyJobListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'job', 'applied_date')
admin.site.register(MyJobList, MyJobListAdmin)

class IsSortListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'job', 'applied_date')
admin.site.register(IsSortList, IsSortListAdmin)