from django.http import (HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect)
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views.generic import FormView, DetailView, ListView
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Gallery, Vote, Shop
from forms import ArtForm
from django.template.context import RequestContext


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


def where_buy(request):
    shops = Shop.objects.all()
    return render(request, 'fcgt/where_buy.html', {
        'shops': shops,
    })

def picture(request, art_id):
    documents = Gallery.objects.get(pk=art_id)
    votes = Vote.objects.filter(art=art_id)
    user1 = Vote.objects.filter(art=art_id)
    user2 = request.user.id
    user3 = False
    for us in votes:
        if us.vote_id == request.user:
            user3 = True
    return render(request, 'fcgt/picture.html', {
            'art_id': art_id,
            'documents': documents,
            'user1':    user1,
            'user2':    user2,
            'user3': user3,
        })

def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('thirdauth/home.html',
                             context_instance=context)

def google(request):
    return render(request, 'fcgt/googlef15025f9fffb7db3.html')

def vote(request, art_id):
    documents = Gallery.objects.get(pk=art_id)
    votes = Vote.objects.filter(art=art_id)
    cat_id = None
    if request.method == 'GET':
        cat_id = art_id
    likes = 0

    for user in votes:
        if user.vote_id == request.user:
            cat_id = None

    if cat_id:
        category = Gallery.objects.get(id=int(cat_id))
        if category:
            likes = category.art_vote + 1
        category.art_vote = likes
        category.save()
        votes1 = Vote()
        votes1.vote_id = request.user
        votes1.art = category
        #votes.vote_id = request.user
        #votes.art = art_id
        votes1.save()

        return render(request, 'fcgt/picture.html', {
        'art_id': art_id,
        'documents': documents,

             })