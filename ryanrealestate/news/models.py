from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from config.mixins import SingleInstanceMixin


class NewsIndexModel(SingleInstanceMixin, models.Model):
    title = models.CharField(
        verbose_name='Blog Index Page Title',
        help_text='This is the title that will be displayed on the page',
        blank=False,
        max_length=120,
    )
    slug = models.SlugField(
        verbose_name='Blog Index Page Slug',
        help_text='This is the blog index page as displayed in the URL.',
        blank=False,
        max_length=120,
    )
    meta_title = models.CharField(
        verbose_name='Page Meta Title',
        help_text='Important for SEO. Include keywords.',
        blank=False,
        max_length=120,
    )
    meta_description = models.CharField(
        verbose_name='Page Meta Description',
        help_text='Important for SEO. Include keywords.',
        blank=False,
        max_length=255,
    )
    description = models.TextField(
        verbose_name='Page Description',
        help_text='This will appear at the top of the page.',
        blank=True,
    )

    class Meta:
        verbose_name = 'Blog Index Page Settings'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse(
            'news:index',
            kwargs={'slug': self.slug},
        )

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super(NewsIndexModel, self).save()

    def __str__(self):
        return self.title


class NewsPostModel(models.Model):
    title = models.CharField(
        verbose_name='Post Title',
        help_text='The title as it appears on the page.',
        blank=False,
        max_length=255,
    )
    slug = models.SlugField()
    meta_title = models.CharField(
        verbose_name='Meta Title',
        help_text='Important for SEO. Include Keywords.',
        blank=False,
        max_length=120,
    )
    meta_description = models.CharField(
        verbose_name='Meta Description',
        help_text='Important for SEO. Include keywords',
        blank=False,
        max_length=255,
    )
    published = models.DateTimeField(
        verbose_name='Publish Date',
        help_text='The date and time the post will go live.',
        auto_now=True,
        blank=False,
    )
    featured_image = models.ImageField(
        verbose_name='Featured Image',
        help_text='Main Image for the post.',
        upload_to='img/news/%Y/%m',
        blank=True,
    )
    author = models.ForeignKey(
        User,
        verbose_name='Author',
        help_text='The user who authored the post.',
        blank=False,
    )
    body = models.TextField(
        verbose_name='Post Body',
        help_text='The main content of the post. HTML OK.',
        blank=True,
    )

    class Meta:
        verbose_name = 'News Post'
        verbose_name_plural = 'News Posts'

    def get_absolute_url(self):
        return reverse(
            'news:post',
            kwargs={'slug': self.slug},
        )

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super(NewsPostModel, self).save()

    def __str__(self):
        return self.title
