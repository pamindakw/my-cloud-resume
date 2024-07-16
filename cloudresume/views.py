from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. You're at the cloud resume.")

# Create your views here.

def home(request):
    return render(request, "base/home.html")
