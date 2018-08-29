# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.contrib import admin
from django.conf.urls import include, url

from . import views

app_name = 'django_db_log'
urlpatterns = [
    # url(r'', TemplateView.as_view(template_name="base.html")),
    url(r'^admin/', include(admin.site.urls)),
]
