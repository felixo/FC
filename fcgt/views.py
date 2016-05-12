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
    documents = Gallery.objects.all()
    return render(request, 'fcgt/gallery.html', {
        'documents': documents
    })


def jury(request):
    return render(request, 'fcgt/jury.html')


def short_rull(request):
    return render(request, 'fcgt/short_rull.html')


def add_art(request):
    if request.method == 'POST':
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fcgt:index'))
    else:
        form = ArtForm()
    return render(request, 'fcgt/add_art.html', {'form': form})
