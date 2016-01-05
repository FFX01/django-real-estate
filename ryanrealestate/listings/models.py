from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

from config.mixins import SingleInstanceMixin


class ListingIndexModel(SingleInstanceMixin, models.Model):
    ORDER_BY_CHOICES = [
        ('date_available', 'Date Available'),
        ('date_published', 'Date Posted'),
        ('price', 'Listing Price'),
    ]
    page_title = models.CharField(
        verbose_name='Listing Index Page Title',
        help_text='The displayed title of the Listing Index Page',
        blank=False,
        null=False,
        max_length=120,
    )
    slug = models.SlugField(
        verbose_name='Listing Index Page Slug',
        help_text='Listing Index Page Title as it appears in the url',
        blank=False,
        null=False,
        max_length=120,
    )
    meta_title = models.CharField(
        verbose_name='Listing Index page Meta Title',
        help_text='Very important for SEO. Include Keywords',
        blank=False,
        null=False,
        max_length=120,
    )
    meta_description = models.CharField(
        verbose_name='Listing Index Page Meta Description',
        help_text='Very important for SEO. Include keywords',
        blank=False,
        null=False,
        max_length=255,
    )
    page_description = models.TextField(
        verbose_name='Page Description',
        help_text='Describe the listings. HTML ok.',
        blank=True,
    )
    order_by = models.CharField(
        verbose_name='Order Listings By',
        choices=ORDER_BY_CHOICES,
        default='date_available',
        max_length=120,
    )

    def get_absolute_url(self):
        return reverse(
            'listings:index',
            kwargs={'index_slug': self.slug},
        )

    def save(self):
        if not self.slug:
            self.slug = slugify(self.page_title)

        super(ListingIndexModel, self).save()

    class Meta:
        verbose_name = 'Listing Index Page Settings'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.page_title


class SoldListingIndexModel(SingleInstanceMixin, models.Model):
    ORDER_BY_CHOICES = [
        ('date_available', 'Date Available'),
        ('date_published', 'Date Posted'),
        ('price', 'Listing Price'),
    ]
    page_title = models.CharField(
        verbose_name='Listing Index Page Title',
        help_text='The displayed title of the Listing Index Page',
        blank=False,
        null=False,
        max_length=120,
    )
    slug = models.SlugField(
        verbose_name='Listing Index Page Slug',
        help_text='Listing Index Page Title as it appears in the url',
        blank=False,
        null=False,
        max_length=120,
    )
    meta_title = models.CharField(
        verbose_name='Listing Index page Meta Title',
        help_text='Very important for SEO. Include Keywords',
        blank=False,
        null=False,
        max_length=120,
    )
    meta_description = models.CharField(
        verbose_name='Listing Index Page Meta Description',
        help_text='Very important for SEO. Include keywords',
        blank=False,
        null=False,
        max_length=255,
    )
    page_description = models.TextField(
        verbose_name='Page Description',
        help_text='Describe the sold listings. HTML ok.',
        blank=True,
    )
    order_by = models.CharField(
        verbose_name='Order Listings By',
        choices=ORDER_BY_CHOICES,
        default='date_available',
        max_length=120,
    )

    def get_absolute_url(self):
        return reverse(
            'listings:sold_index',
            kwargs={'index_slug': self.slug},
        )

    def save(self):
        if not self.slug:
            self.slug = slugify(self.page_title)

        super(SoldListingIndexModel, self).save()

    class Meta:
        verbose_name = 'Sold Listing Index Page Settings'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.page_title

class ListingModel(models.Model):
    name = models.CharField(
        verbose_name='Listing Name',
        help_text='Listing Street Address',
        null=False,
        blank=False,
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name='Listing Slug',
        help_text='Listing name as it appears in the url',
        blank=False,
        null=False,
    )
    meta_title = models.CharField(
        verbose_name='Meta Title',
        help_text='A Title with Keywords for SEO',
        max_length=120,
    )
    meta_description = models.CharField(
        verbose_name='Meta Description',
        help_text='A Description for SEO purposes',
        max_length=255,
    )
    main_image = models.ImageField(
        verbose_name='Featured Image',
        help_text='Primary Image for the listing',
        upload_to='img/listings/%Y/%m',
    )
    date_published = models.DateField(
        verbose_name='Date Posted',
        auto_now_add=True,
        blank=False,
        null=False,
    )
    date_available = models.DateField(
        verbose_name='Date Available',
        blank=True,
    )
    is_sold = models.BooleanField(
        verbose_name='Is Sold?',
        help_text='Check this box if the property has been sold',
        default=False,
    )
    date_sold = models.DateField(
        verbose_name='Date Sold',
        help_text='The date the property was sold',
        blank=True,
        null=True,
    )
    price = models.IntegerField(
        verbose_name='Listing Price',
        blank=True,
    )
    location = models.CharField(
        verbose_name='Listing Location',
        help_text='Full Address of the property',
        blank=False,
        null=False,
        max_length=255,
    )
    property_description = models.TextField(
        verbose_name='Property Description',
        help_text='A description of the home/apartment',
    )
    neighborhood_description = models.TextField(
        verbose_name='Neighborhood Description',
        help_text='A description of the property neighborhood',
    )

    class Meta:
        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'

    def get_absolute_url(self):
        return reverse(
            'listings:listing',
            kwargs={'slug': self.slug},
        )

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)

        super(ListingModel, self).save()

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    title = models.CharField(
        verbose_name='Image Title',
        blank=True,
        max_length=120,
    )
    description = models.CharField(
        verbose_name='Image Description',
        blank=True,
        max_length=120,
    )
    image = models.ImageField(
        verbose_name='Image',
        blank=False,
        null=False,
        upload_to='img/gallery/%Y/%m',
    )
    parent = models.ForeignKey(
        ListingModel,
        on_delete=models.CASCADE,
        related_name='gallery_image',
    )

    class Meta:
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'
