from django.shortcuts import render

# Create your views here.
def csedept(request):
    return render(request,'csedept.html')

def csestudents(request):
    return render(request,'csestudents.html')