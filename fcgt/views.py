from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from .models import Gallery, Vote
from .forms import UploadFileForm
from forms import handle_uploaded_file


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

def add_art(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('fcgt/index.html', {'form': form})