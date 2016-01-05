from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^properties/(?P<slug>.*)/$',
        views.ListingView.as_view(),
        name='listing',
    ),
    url(
        r'^sold/(?P<index_slug>.*)/$',
        views.SoldListingIndexView.as_view(),
        name='sold_index',
    ),
    url(
        r'^(?P<index_slug>.*)/$',
        views.ListingIndexView.as_view(),
        name='index',
    ),
]