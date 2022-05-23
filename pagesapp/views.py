from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPagevIEW(TemplateView):
    template_name = 'about.html'

class CallPageView(TemplateView):
    template_name = 'call.html'


class TestClass(TemplateView):
    pass