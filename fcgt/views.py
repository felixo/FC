from django.http import (HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect)
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views.generic import FormView, DetailView, ListView
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Gallery, Gallery2, Vote, Shop
from forms import ArtForm
from django.template.context import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    # question = get_object_or_404(Question, pk=question_id)
    form = ArtForm()
    return render(request, 'fcgt/index.html',  {'form': form})


def awards(request):
    return render(request, 'fcgt/awards.html')


def full_rull(request):
    return render(request, 'fcgt/full_rull.html')


def gallery(request):
    obj = Gallery2.objects.filter(art_category="monochrome_lab")
    print obj
    paginator = Paginator(obj, 15)
    page = request.GET.get('page')

    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)

    index = documents.number - 1  # edited to something easier without index
        # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
        # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
        # My new page range
    page_range = list(paginator.page_range)
    page_range = page_range[start_index:end_index]

    return render(request, 'fcgt/gallery.html', {
        'documents': documents,
        'page_range': page_range,
            })

def gallery2(request):
    obj = Gallery2.objects.filter(art_category="polychrome_planet")
    print obj
    paginator = Paginator(obj, 15)
    page = request.GET.get('page')

    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)

    index = documents.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    # My new page range
    page_range = list(paginator.page_range)
    page_range = page_range[start_index:end_index]

    return render(request, 'fcgt/gallery2.html', {
        'documents': documents,
        'page_range': page_range,
    })

def gallery3(request):
    obj = Gallery2.objects.filter(art_category="pitt_artist")
    print obj
    paginator = Paginator(obj, 15)
    page = request.GET.get('page')

    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)

    index = documents.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    # My new page range
    page_range = list(paginator.page_range)
    page_range = page_range[start_index:end_index]

    return render(request, 'fcgt/gallery3.html', {
        'documents': documents,
        'page_range': page_range,
    })

def gallery4(request):
    obj = Gallery2.objects.filter(art_category="albrecht_durer")
    print obj
    paginator = Paginator(obj, 15)
    page = request.GET.get('page')

    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)

    index = documents.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    # My new page range
    page_range = list(paginator.page_range)
    page_range = page_range[start_index:end_index]

    return render(request, 'fcgt/gallery4.html', {
        'documents': documents,
        'page_range': page_range,
    })

def gallery5(request):
    obj = Gallery2.objects.filter(art_category="connector")
    print obj
    paginator = Paginator(obj, 15)
    page = request.GET.get('page')

    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)

    index = documents.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    # My new page range
    page_range = list(paginator.page_range)
    page_range = page_range[start_index:end_index]

    return render(request, 'fcgt/gallery5.html', {
        'documents': documents,
        'page_range': page_range,
    })

def gallery6(request):
    obj = Gallery2.objects.filter(art_category="little_castle")
    print obj
    paginator = Paginator(obj, 15)
    page = request.GET.get('page')

    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documents = paginator.page(paginator.num_pages)

    index = documents.number - 1  # edited to something easier without index
    # This value is maximum index of your pages, so the last page - 1
    max_index = len(paginator.page_range)
    # You want a range of 7, so lets calculate where to slice the list
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    # My new page range
    page_range = list(paginator.page_range)
    page_range = page_range[start_index:end_index]

    return render(request, 'fcgt/gallery6.html', {
        'documents': documents,
        'page_range': page_range,
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
            new_art = form.save()
            art_id = new_art.id
            return HttpResponseRedirect(reverse('fcgt:picture', args=[art_id]))
    else:
        form = ArtForm()
    return render(request, 'fcgt/index.html', {'form': form})


def where_buy(request):
    shops = Shop.objects.all()
    return render(request, 'fcgt/where_buy.html', {
        'shops': shops,
    })

def picture(request, art_id):
    documents = Gallery2.objects.get(pk=art_id)
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
    documents = Gallery2.objects.get(pk=art_id)
    votes = Vote.objects.filter(art=art_id)
    cat_id = None
    if request.method == 'GET':
        cat_id = art_id
    likes = 0

    for user in votes:
        if user.vote_id == request.user:
            cat_id = None

    if cat_id:
        category = Gallery2.objects.get(id=int(cat_id))
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

def karlbox(request):
    return render(request,'fcgt/karlbox.html')