from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'site/index.html')
