from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from hr.models import JobPost, CandidateApplication, SelectCandidate

# Create your views here.

@login_required
def HrHome(request):
    return render(request, 'hr/hrdashboard.html')

@login_required
def post_job(request):
    msg = None
    if request.method == 'POST':
        job_title = request.POST.get('job-title')
        address = request.POST.get('address')
        company_name = request.POST.get('company-name')
        low_salary = request.POST.get('salary-low')
        high_salary = request.POST.get('salary-high')
        last_date = request.POST.get('last-date')

        job_post = JobPost(user=request.user, title=job_title, address=address, company_name=company_name, salary_low=low_salary, salary_high=high_salary, last_date=last_date)
        msg = 'Job Added Successfull!'
        job_post.save()
        #print(job_title, address, company_name)

    context = {'msg':msg}
    return render(request, 'hr/postjob.html', context)

@login_required
def candidate_detail(request, pk):
    print(pk)
    return render(request, 'hr/candidate.html')