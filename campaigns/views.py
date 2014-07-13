from django.shortcuts import render_to_response
from django.conf import settings
from django.template.context import RequestContext
from django.core.context_processors import csrf
from django.views.decorators.clickjacking import xframe_options_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
import changeorg

from campaigns.models import Campaign
from campaigns.forms import *

corg = changeorg.Client(api_key=settings.CHANGEORG_API_KEY,
    api_secret=settings.CHANGEORG_API_SECRET)

# Create your views here.

@xframe_options_exempt
def campaigns_widget(request):
    campaigns = Campaign.objects.filter(public=True).order_by('-signature_count')
    paginator = Paginator(campaigns, 3)
    page = request.GET.get('page')
    try:
        campaigns = paginator.page(page)
    except PageNotAnInteger:
        campaigns = paginator.page(1)
    except EmptyPage:
        campaigns = paginator.page(paginator.num_pages)
    c = {"campaigns":campaigns}
    return render_to_response("campaigns/campaigns_widget.html",c,
        context_instance= RequestContext(request))

@xframe_options_exempt
def add_widget(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("campaigns/thanks.html",{},
                    context_instance=RequestContext(request))
    else:
        form = CampaignForm()
    urlform = AddFromURLForm()
    c={
        "form": form,
        "urlform": urlform }
    c.update(csrf(request))
    return render_to_response("campaigns/add_widget.html",c,
        context_instance=RequestContext(request))

@xframe_options_exempt
def add_from_url_widget(request):
    if request.method == 'POST':
        form = AddFromURLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            cid = corg.get_petition_id(url)
            petition = corg.get_petition(cid)
            print petition
            c = Campaign()
            c.change_id = petition['petition_id']
            c.title = petition['title']
            c.url = petition['url']
            c.overview=petition['overview']
            c.signature_count=petition['signature_count']
            c.image_url=petition['image_url']
            c.save()
            return render_to_response("campaigns/thanks.html", {},
                    context_instance = RequestContext(request))
    else:
        return HttpResponseRedirect('../add')
