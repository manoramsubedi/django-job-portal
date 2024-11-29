from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register_candidate(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password != cpassword:
            msg = "Password doesn't match!!"
            return render (request, 'authuser/candidate_register.html',{'msg':msg})

        if User.objects.filter(username=username).exists():
            msg="User already exist!"
            return render (request, 'authuser/candidate_register.html',{'msg':msg})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('candidate_dashboard')

    return render(request, 'authuser/candidate_register.html')

def register_hr(request):
    return render(request, 'authuser/hr_register.html')
