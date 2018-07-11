from sites.models import Site, SiteValues
from django.views.generic import ListView, DetailView
from django.template.response import  TemplateResponse
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Sum