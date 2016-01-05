from django.db import models
from django.template.defaultfilters import slugify


class MenuModel(models.Model):
    name = models.CharField(
        verbose_name='Menu Name',
        help_text='The name of the menu',
        blank=False,
        null=False,
        max_length=120,
    )
    slug = models.SlugField()

    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(MenuModel, self).save()

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.name


class MenuItemModel(models.Model):
    name = models.CharField(
        verbose_name='Menu Item Name',
        help_text='The display name of the menu item',
        blank=False,
        null=False,
        max_length=80,
    )
    link = models.URLField(
        verbose_name='Link',
        help_text='Where the menu item will link to.',
        blank=True,
    )
    order = models.IntegerField(
        verbose_name='Item Index',
        help_text='The order of the menu items. e.g. Set to 0 for first, 100 for last.',
        blank=False,
        null=False,
    )
    menu = models.ForeignKey(
        MenuModel,
        verbose_name='Parent Menu',
        help_text='The menu this item will be a part of.',
        related_name='menu_item',
    )

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return self.name
