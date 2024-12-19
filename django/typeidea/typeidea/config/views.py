from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView

from blog.views import CommonViewMixin
from .models import Link


def links(request):
    return HttpResponse('links')


class LinkListView(CommonViewMixin, ListView):
    model = Link
    template_name = 'config/links.html'



