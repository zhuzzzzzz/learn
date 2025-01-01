"""
URL configuration for typeidea project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from .custom_site import custom_site
from blog.views import IndexView
from config.views import links, LinkListView
from comment.views import CommentView

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),

    re_path(r'^links/$', LinkListView.as_view(), name='links'),
    re_path(r'^comment/$', CommentView.as_view(), name='comment'),

    path('blog/', include('blog.urls')),
    path('super_admin/', admin.site.urls, name='super-admin'),
    path('admin/', custom_site.urls, name='admin'),
]
