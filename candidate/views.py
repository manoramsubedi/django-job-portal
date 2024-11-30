from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from hr.models import JobPost

# Create your views here.

@login_required
def candidate_dashboard(request):
    jobs = JobPost.objects.all()
    context = {
        'jobs':jobs,
    }
    return render(request, 'candidate/dashboard.html', context)

@login_required
def joblist(request):
    return render(request, 'candidate/joblist.html')

@login_required
def applyforjob(request, pk):
    print(pk)
    return render(request, 'candidate/jobapply.html')