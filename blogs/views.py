from django.shortcuts import render

def home(request):
    return render(request, 'blogs/index.html')