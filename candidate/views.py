from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import MyJobList
from hr.models import JobPost, CandidateApplication, Hr

# Create your views here.

@login_required
def candidate_dashboard(request):
    if Hr.objects.filter(user=request.user).exists():
        return redirect('hrdash')

    jobs = JobPost.objects.all()
    context = {
        'jobs':jobs,
    }
    return render(request, 'candidate/dashboard.html', context)

@login_required
def joblist(request):
    if Hr.objects.filter(user=request.user).exists():
        return redirect('hrdash')

    joblist = MyJobList.objects.filter(user=request.user)
    context = {
        'joblist':joblist
    }
    return render(request, 'candidate/joblist.html', context)

@login_required
def applyforjob(request, pk):
    if Hr.objects.filter(user=request.user).exists():
        return redirect('hrdash')
    
    if JobPost.objects.filter(id=pk).exists():
        job = JobPost.objects.get(id=pk)
        if CandidateApplication.objects.filter(user=request.user, job=job).exists():
            return redirect('candidate_dashboard')

        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            college = request.POST.get('college')
            passing_year = request.POST.get('passing_year')
            yearOfExperience =request.POST.get('yearOfExperience')
            resume = request.FILES.get('resume')

            candidate_applicaction = CandidateApplication(user=request.user, job=job, pass_year=passing_year, experience=yearOfExperience, resume=resume)
            candidate_applicaction.save()
            MyJobList(user=request.user, job=candidate_applicaction).save()
            return redirect('candidate_dashboard')

    return render(request, 'candidate/jobapply.html')