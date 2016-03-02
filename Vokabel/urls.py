"""PyLatein URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r"^$", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r"^$", Home.as_view(), name="home")
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r"^blog/", include(blog_urls))
"""
from django.conf.urls import url
import Vokabel.views

# app_name="vokabel"
urlpatterns = [
    url(r"search", Vokabel.views.SearchView.as_view(), name="search"),
    url(r"createNoun$", Vokabel.views.CreateNoun.as_view(), name="create_noun"),
    url(r"noun(?P<pk>[0-9]+)$", Vokabel.views.NounDetail.as_view(), name="view_noun"),
    url(r"createVerb$", Vokabel.views.CreateVerb.as_view(), name="create_verb"),
    url(r"verb(?P<pk>[0-9]+)$", Vokabel.views.VerbDetail.as_view(), name="view_verb"),
    url(r"createAdjective$", Vokabel.views.CreateAdjective.as_view(), name="create_adjective"),
    url(r"adjective(?P<pk>[0-9]+)$", Vokabel.views.AdjectiveDetail.as_view(), name="view_adjective"),
    url(r"createVocGr$", Vokabel.views.CreateVocGroup.as_view(), name="create_vocgroup"),
]
