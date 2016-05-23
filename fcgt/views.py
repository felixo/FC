from django.http import (HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect)
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views.generic import FormView, DetailView, ListView
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Gallery, Vote
from forms import ArtForm


def index(request):
    # question = get_object_or_404(Question, pk=question_id)
    form = ArtForm()
    return render(request, 'fcgt/index.html',  {'form': form})


def awards(request):
    return render(request, 'fcgt/awards.html')


def full_rull(request):
    return render(request, 'fcgt/full_rull.html')


def gallery(request):
    documents = Gallery.objects.filter(art_category="BlackAndWhite")
    return render(request, 'fcgt/gallery.html', {
        'documents': documents
    })

def gallery2(request):
    documents = Gallery.objects.filter(art_category="ProfiVsHobby")
    return render(request, 'fcgt/gallery2.html', {
        'documents': documents
    })

def gallery3(request):
    documents = Gallery.objects.filter(art_category="Scatching")
    return render(request, 'fcgt/gallery3.html', {
        'documents': documents
    })

def gallery4(request):
    documents = Gallery.objects.filter(art_category="CopyPast")
    return render(request, 'fcgt/gallery4.html', {
        'documents': documents
    })

def gallery5(request):
    documents = Gallery.objects.filter(art_category="MiniArt")
    return render(request, 'fcgt/gallery5.html', {
        'documents': documents
    })

def jury(request):
    return render(request, 'fcgt/jury.html')


def short_rull(request):
    form = ArtForm()
    return render(request, 'fcgt/short_rull.html',  {'form': form})


def add_art(request):
    if request.method == 'POST':
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fcgt:index'))
    else:
        form = ArtForm()
    return render(request, 'fcgt/index.html', {'form': form})
