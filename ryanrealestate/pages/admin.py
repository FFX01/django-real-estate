from django.contrib import admin

from . import models


@admin.register(models.ContentPageModel)
class ContentPageModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }
