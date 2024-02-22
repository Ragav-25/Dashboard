from django.shortcuts import render

def dashboard(request):
    return render(request,'Inv/dashboard.html')