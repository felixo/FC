from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'fcgt.views.index', name='index'),
    url(r'^jury/', 'fcgt.views.jury', name='jury'),
    url(r'^nagradi/', 'fcgt.views.awards', name='nagradi'),
    url(r'^pravila/', 'fcgt.views.full_rull', name='rules'),
    url(r'^black_and_white/', 'fcgt.views.gallery', name='gallery'),
    url(r'^uchastnikam/', 'fcgt.views.short_rull', name='uchastnikam'),
    url(r'^add_art/', 'fcgt.views.add_art', name='add_art'),
    url(r'^colors/', 'fcgt.views.gallery2', name='gallery2'),
    url(r'^sketch/', 'fcgt.views.gallery3', name='gallery3'),
    url(r'^copy_past/', 'fcgt.views.gallery4', name='gallery4'),
    url(r'^mini_art/', 'fcgt.views.gallery5', name='gallery5'),
    url(r'^where_buy/', 'fcgt.views.where_buy', name='where_buy'),
    url(r'^picture/(?P<art_id>\d+)/$', 'fcgt.views.picture', name='picture'),
    url(r'^picture/(?P<art_id>\d+)/vote$', 'fcgt.views.vote', name='vote'),
]