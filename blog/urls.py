from . import views
from django.urls import include

from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path('about', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView, name='contact'),
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]

