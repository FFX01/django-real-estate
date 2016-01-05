from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from . import models


class HomeView(View):

    def get(self, request):
        page = models.HomeModel.objects.all().first()
        context = {
            'meta_title': page.meta_title,
            'meta_description': page.meta_description,
            'page': page,
        }

        return render(
            request,
            'home/home.html',
            context,
        )
