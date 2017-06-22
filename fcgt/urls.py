from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jury/', views.jury, name='jury'),
    url(r'^nagradi/', views.awards, name='nagradi'),
    url(r'^pravila/', views.full_rull, name='rules'),
    url(r'^monochrome_lab/', views.gallery, name='gallery'),
    url(r'^uchastnikam/', views.short_rull, name='uchastnikam'),
    url(r'^add_art/', views.add_art, name='add_art'),
    url(r'^polychrome_planet/', views.gallery2, name='gallery2'),
    url(r'^pitt_artist/', views.gallery3, name='gallery3'),
    url(r'^albrecht_durer/', views.gallery4, name='gallery4'),
    url(r'^connector/', views.gallery5, name='gallery5'),
    url(r'^little_castle/', views.gallery6, name='gallery6'),
    url(r'^where_buy/', views.where_buy, name='where_buy'),
    url(r'^googlef15025f9fffb7db3.html/', views.google, name='google'),
    url(r'^picture/(?P<art_id>\d+)/$', views.picture, name='picture'),
    url(r'^picture/(?P<art_id>\d+)/vote$', views.vote, name='vote'),
    url(r'^karlbox/', views.karlbox, name='karlbox'),
    url(r'^delete/(?P<art_id>\d+)/$', views.delete, name='delete'),
]
