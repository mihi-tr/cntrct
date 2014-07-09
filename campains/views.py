from django.shortcuts import render_to_response
from django.conf import settings
from django.views.decorators.clickjacking import xframe_options_exempt
import changeorg

from campains.models import Campain


# Create your views here.

@xframe_options_exempt
def campaings_widget(request):
    pass

@xframe_options_exempt
def add_widget(request):
    pass

@xframe_options_exempt
def add_from_url_widget(request):
    pass
