from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import ContentPageModel
from .forms import ContactForm


class PageView(View):

    def get(self, request, path, instance):
        context = {
            'instance': instance,
            'children': instance.get_children() if instance else ContentPageModel.objects.root_nodes(),
            'meta_title': instance.meta_title,
            'meta_description': instance.meta_description,
        }

        return render(
            request,
            'pages/content_page.html',
            context,
        )


class ContactView(View):

    def get(self, request):
        context = {
            'page_title': 'Contact Us',
            'meta_title': "Prestige Local Properties | Contact Us",
            'meta_description': "Contact Prestige Local Properties",
            'contact_form': ContactForm(),
        }

        return render(
            request,
            'pages/contact.html',
            context
        )

    def post(self, request):
        send_mail(
            'New Client Contact for Prestige Local Properties',
            "%s --- %s" % (request.POST['email'], request.POST['message']),
            request.POST['email'],
            ['walters.justin01@gmail.com'],
        )

        return HttpResponseRedirect(
            reverse('pages:thank_you'),
        )


class ThankYouView(View):
    def get(self, request):
        context = {
            'page_title': 'Thank You!',
            'meta_title': 'Prestige Local Properties | Thank you for contacting us',
            'meta_description': 'Thank you for contacting Prestige Local Properties.',
        }
        return render(
            request,
            'pages/thank_you.html',
            context,
        )