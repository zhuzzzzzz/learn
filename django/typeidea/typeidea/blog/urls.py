from django.urls import path, re_path
from . import views
from . import rss
from django.contrib.sitemaps import views as sitemap_views
# from . import sitemap
from .sitemap import PostSitemap

app_name = 'blog'
urlpatterns = [
    path('latest', views.IndexView.as_view(), name='latest'),
    path('hottest', views.HostView.as_view(), name='hottest'),
    re_path(r'^category/(?P<category_id>\d+)/$', views.CategoryView.as_view(), name='category-list'),
    re_path(r'^tag/(?P<tag_id>\d+)/$', views.TagView.as_view(), name='tag-list'),
    re_path(r'^post/(?P<post_id>\d+).html$', views.PostDetailView.as_view(), name='post-detail'),
    re_path(r'^search/$', views.SearchView.as_view(), name='search'),
    re_path(r'^author/(?P<owner_id>\d+)/$', views.AuthorView.as_view(), name='author'),

    re_path(r'^rss|feed/$', rss.LatestPostFeed(), name='rss'),
    re_path(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
]
