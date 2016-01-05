from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'posts/(?P<slug>.*)/$',
        views.NewsPostView.as_view(),
        name='post',
    ),
    url(
        r'(?P<slug>.*)/$',
        views.NewsIndexView.as_view(),
        name='index',
    ),
]
