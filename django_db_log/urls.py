# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf.urls import include, url

app_name = 'django_db_log'
urlpatterns = [
    # url(r'', ErrorListView.as_view(), name='error_list'),
    # url(r'', TemplateView.as_view(template_name="base.html")),
    url(r'admin/', include(admin.site.urls)),
]
