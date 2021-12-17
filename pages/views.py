# imports
# from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# home template
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


