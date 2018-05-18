from django.shortcuts import render
from django.template.context_processors import request

# Create your views here.
def main(request):
    return render(request, 'main/main.html')

def rull(request):
    return render(request, 'main/rull.html')

def gett(request):
    return render(request, 'main/gett.html')

def live(request):
    return render(request, 'main/live.html')

def logo(request):
    return render(request, 'main/logo.html')

def index(request):
    return render(request, 'main/index.html')

def pergramme(request):
    return render(request, 'main/pergramme.html')