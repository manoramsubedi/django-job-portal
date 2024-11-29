from django.shortcuts import render

# Create your views here.

def candidate_dashboard(request):
    return render(request, 'candidate/dashboard.html')
