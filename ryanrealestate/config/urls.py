from django.conf.urls import url, include
from django.contrib import admin
from django.views import static

from . import settings

urlpatterns = [
    url(
        r'^media/(?P<path>.*)$',
        static.serve,
        {'document_root': settings.MEDIA_ROOT},
    ),
    url(
        r'^admin/',
        admin.site.urls
    ),
    url(
        r'^listings/',
        include(
            'listings.urls',
            namespace='listings'
        ),
    ),
    url(
        r'^news/',
        include(
            'news.urls',
            namespace='news',
        ),
    ),
    url(
        r'^',
        include(
            'home.urls',
            namespace='home',
        ),
    ),
    url(
        r'',
        include(
            'pages.urls',
            namespace='pages',
        ),
    ),
]
