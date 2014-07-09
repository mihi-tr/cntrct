from django.shortcuts import render_to_response
from django.conf import settings
from django.template.context import RequestContext
from django.core.context_processors import csrf
from django.views.decorators.clickjacking import xframe_options_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
import changeorg

from campaigns.models import Campaign


# Create your views here.

@xframe_options_exempt
def campaigns_widget(request):
    campaigns = Campaign.objects.filter(public=True)
    paginator = Paginator(contact_list, 4)
    page = request.GET.get('page')
    try:
        campaigns = paginator.page(page)
    except PageNotAnInteger:
        campaigns = paginator.page(1)
    except EmptyPage:
        campaigns = paginator.page(paginator.num_pages)
    c = {"campaigns":campaigns}
    return render_to_response("campaigns/campaigns_widget.html,c,
        context_instance= RequestContext(request))

@xframe_options_exempt
def add_widget(request):
    if request.method == 'POST':
        pass
    
    c={}
    c.update(csrf(request))
    return render_to_response("campaignns/add_widget.html",c,
        context_instance=RequestContext(request))

@xframe_options_exempt
def add_from_url_widget(request):
    if request.method == 'POST':
        pass
    else:
        return HttpResponseRedirect('../add')
