from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'fcgt.views.index', name='index'),
    url(r'^jury/', 'fcgt.views.jury', name='jury'),
    url(r'^nagradi/', 'fcgt.views.awards', name='nagradi'),
    url(r'^pravila/', 'fcgt.views.full_rull', name='rules'),
    url(r'^gallery/', 'fcgt.views.gallery', name='gallery'),
    url(r'^uchastnikam/', 'fcgt.views.short_rull', name='uchastnikam'),
    url(r'^add_art/', 'fcgt.views.add_art', name='add_art'),
]