from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from .models import Gallery, Vote
from .forms import ImageUploadForm
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView
from django.http import HttpResponse, HttpResponseForbidden
from django.utils import timezone


def index(request):
    #question = get_object_or_404(Question, pk=question_id)
    return render(request, 'fcgt/index.html')

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
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            #return HttpResponse(request.FILES)
            newdoc = Gallery(docfile = request.FILES['image'])
            newdoc.pub_date = timezone.now()
            newdoc.docfile.name = 'Img_%s.jpg' % newdoc.pk
            return HttpResponse(newdoc.pk)
            newdoc.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')