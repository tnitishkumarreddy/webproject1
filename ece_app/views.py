from django.shortcuts import render

# Create your views here.
def ecedept(request):
    return render(request,'ecedept.html')

def ecestudents(request):
    return render(request,'ecestudents.html')