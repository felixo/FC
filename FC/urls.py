"""FC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'fcgt.views.index', name='main'),
    url(r'^jury/', 'fcgt.views.jury', name='jury'),
    url(r'^admin/', admin.site.urls),
    url(r'^nagradi/', 'fcgt.views.awards', name='nagradi'),
    url(r'^pravila/', 'fcgt.views.full_rull'),
    url(r'^gallery/', 'fcgt.views.gallery', name='gallery'),
    url(r'^uchastnikam/', 'fcgt.views.short_rull'),
    url(r'^add_art/', 'fcgt.views.add_art', name='add_art'),
]