from django.contrib import admin

from . import models


class MenuItemInline(admin.TabularInline):
    model = models.MenuItemModel


@admin.register(models.MenuModel)
class MenuModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
    inlines = [
        MenuItemInline,
    ]
