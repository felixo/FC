from django.shortcuts import get_object_or_404, render

from .models import Gallery, Vote

def index(request):
    #question = get_object_or_404(Question, pk=question_id)
    return render(request, 'fcgt/index.html')


# Create your views here.
