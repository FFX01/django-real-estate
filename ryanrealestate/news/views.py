from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from . import models


class NewsIndexView(View):
    """
    Renders an index page for news posts. Posts are paginated in steps of 10.
    """
    def get(self, request, slug):
        page_instance = models.NewsIndexModel.objects.get(slug=slug)
        post_list = models.NewsPostModel.objects.all()
        paginator = Paginator(post_list, 10)  # Show 10 posts per page
        page = request.GET.get('page')
        try:
            listings = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            listings = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            listings = paginator.page(paginator.num_pages)
        context = {
            'meta_title': page_instance.meta_title,
            'meta_description': page_instance.meta_description,
            'page_instance': page_instance,
            'listings': listings,
        }
        return render(
            request,
            'news/index.html',
            context,
        )


class NewsPostView(View):
    """
    Renders a page for displaying individual news posts.
    """
    def get(self, request, slug):
        post = models.NewsPostModel.objects.get(slug=slug)
        context = {
            'meta_title': post.meta_title,
            'meta_description': post.meta_description,
            'post': post,
        }
        return render(
            request,
            'news/post.html',
            context,
        )