from django.contrib import admin

from config.mixins import SingleInstanceAdminMixin
from . import models


@admin.register(models.NewsIndexModel)
class NewsIndexModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }


@admin.register(models.NewsPostModel)
class NewsPostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }
