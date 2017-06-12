from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jury/', views.jury, name='jury'),
    url(r'^nagradi/', views.awards, name='nagradi'),
    url(r'^pravila/', views.full_rull, name='rules'),
    url(r'^black_and_white/', views.gallery, name='gallery'),
    url(r'^uchastnikam/', views.short_rull, name='uchastnikam'),
    url(r'^add_art/', views.add_art, name='add_art'),
    url(r'^colors/', views.gallery2, name='gallery2'),
    url(r'^sketch/', views.gallery3, name='gallery3'),
    url(r'^copy_past/', views.gallery4, name='gallery4'),
    url(r'^mini_art/', views.gallery5, name='gallery5'),
    url(r'^where_buy/', views.where_buy, name='where_buy'),
    url(r'^googlef15025f9fffb7db3.html/', views.google, name='google'),
    url(r'^picture/(?P<art_id>\d+)/$', views.picture, name='picture'),
    url(r'^picture/(?P<art_id>\d+)/vote$', views.vote, name='vote'),
]
