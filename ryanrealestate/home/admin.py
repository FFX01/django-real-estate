from django.contrib import admin

from . import models
from config.mixins import SingleInstanceAdminMixin


@admin.register(models.HomeModel)
class HomeModelAdmin(SingleInstanceAdminMixin, admin.ModelAdmin):
    pass
