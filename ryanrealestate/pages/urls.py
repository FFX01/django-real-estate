from django.conf.urls import url

import mptt_urls

from . import views

urlpatterns = [
    url(
        r'^contact/thank-you/$',
        views.ThankYouView.as_view(),
        name='thank_you',
    ),
    url(
        r'^contact/$',
        views.ContactView.as_view(),
        name='contact',
    ),
    url(
        r'^(?P<path>.*)$',
        mptt_urls.view(
            model='pages.models.ContentPageModel',
            view=views.PageView.as_view(),
            slug_field='slug',
        ),
        name='page_view',
    ),
]