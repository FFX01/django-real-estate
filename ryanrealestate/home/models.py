from django.db import models
from django.core.urlresolvers import reverse

from config.mixins import SingleInstanceMixin


class HomeModel(SingleInstanceMixin, models.Model):
    """
    This is the model for the site homepage. Allows for user to change page
    settings and layout on the fly from django admin.
    """
    page_title = models.CharField(
        verbose_name='Homepage Title',
        help_text='The Page title as it appears on the page',
        blank=False,
        null=False,
        max_length=120,
    )
    meta_title = models.CharField(
        verbose_name='Homepage Meta Title',
        help_text='Very important for SEO. Include keywords.',
        blank=False,
        null=False,
        max_length=120,
    )
    meta_description = models.CharField(
        verbose_name='Homepage Meta Description',
        help_text='Very important for SEO. Include keywords.',
        blank=False,
        null=False,
        max_length=255,
    )
    body = models.TextField()

    def get_absolute_url(self):
        return reverse(
            'home:home',
        )

    class Meta:
        verbose_name = 'Homepage Settings'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.page_title
