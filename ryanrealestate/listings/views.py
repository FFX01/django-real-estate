from django.shortcuts import render
from django.views.generic import View

from .models import ListingIndexModel, SoldListingIndexModel, ListingModel


class ListingIndexView(View):

    def get(self, request, *args, **kwargs):
        page = ListingIndexModel.objects.get(slug=kwargs['index_slug'])
        listings = ListingModel.objects.order_by(page.order_by)
        context ={
            'meta_title': page.meta_title,
            'meta_description': page.meta_description,
            'listings': listings,
            'page': page,
        }

        return render(
            request,
            'listings/listing_index.html',
            context,
        )


class SoldListingIndexView(View):

    def get(self, request, *args, **kwargs):
        page = SoldListingIndexModel.objects.get(slug=kwargs['index_slug'])
        listings = ListingModel.objects.order_by(page.order_by)
        context ={
            'meta_title': page.meta_title,
            'meta_description': page.meta_description,
            'listings': listings,
            'page': page,
        }

        return render(
            request,
            'listings/sold_listing_index.html',
            context,
        )


class ListingView(View):

    def get(self, request, *args, **kwargs):
        listing = ListingModel.objects.get(slug=kwargs['slug'])
        context = {
            'meta_title': listing.meta_title,
            'meta_description': listing.meta_description,
            'listing': listing,
        }

        return render(
            request,
            'listings/listing.html',
            context,
        )


