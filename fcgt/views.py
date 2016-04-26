from django.shortcuts import get_object_or_404, render

from .models import Gallery, Vote

def index(request):
    #question = get_object_or_404(Question, pk=question_id)
    return render(request, 'fcgt/index.html')

def awards(request):
    return render(request, 'fcgt/awards.html')

def full_rull(request):
    return render(request, 'fcgt/full_rull.html')

def gallery(request):
    return render(request, 'fcgt/gallery.html')

def jury(request):
    return render(request, 'fcgt/jury.html')

def short_rull(request):
    return render(request, 'fcgt/short_rull.html')
# Create your views here.
