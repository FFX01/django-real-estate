from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

from mptt.models import MPTTModel, TreeForeignKey


class BasePageModel(MPTTModel):
    title = models.CharField(
        verbose_name='Page Title',
        help_text='Page Title as it appears on the page.',
        blank=False,
        null=False,
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name='Page slug',
        help_text='The Page name as it appears in the url.',
    )
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        verbose_name='Parent Page',
        related_name='children',
        db_index=True,
    )
    published = models.DateTimeField(
        verbose_name='Page Published',
        help_text='The date the page is published.',
        auto_now=True,
    )
    status = models.BooleanField(
        verbose_name='Page is live',
        help_text='Check this box to make the page available to the public.',
        default=True,
    )
    meta_title = models.CharField(
        verbose_name='Page Meta Title',
        help_text='Very important for SEO. Include keywords.',
        blank=False,
        null=False,
        max_length=120,
    )
    meta_description = models.CharField(
        verbose_name='Page Meta Description',
        help_text='Very important for SEO. Include keywords.',
        blank=False,
        null=False,
        max_length=255,
    )

    def get_absolute_url(self):
        return reverse(
            'pages:page_view',
            kwargs={
                'path': self.get_path()
            }
        )

    class MPTTMeta:
        order_insertion_by = [
            'title'
        ]

    class Meta:
        abstract = True

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)

        super(BasePageModel, self).save()


class ContentPageModel(BasePageModel):
    body = models.TextField()

    class Meta:
        verbose_name = 'Content Page'
        verbose_name_plural = 'Content Pages'

    def __str__(self):
        return self.title