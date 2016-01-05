from django.contrib import admin

from . import models
from config.mixins import SingleInstanceAdminMixin


class GalleryImageInline(admin.TabularInline):
    model = models.GalleryImage


@admin.register(models.ListingIndexModel)
class ListingIndexAdmin(SingleInstanceAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('page_title',)
    }


@admin.register(models.SoldListingIndexModel)
class ListingIndexAdmin(SingleInstanceAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('page_title',)
    }


@admin.register(models.ListingModel)
class ListingModelAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_published'
    prepopulated_fields = {
        'slug': ('name',)
    }
    inlines = [
        GalleryImageInline,
    ]
