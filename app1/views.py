from copy import deepcopy

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class T1(TemplateView):
    """
    This view does nothing. Its a templateview
    """
    template_name = 'app1/homepage.html'

