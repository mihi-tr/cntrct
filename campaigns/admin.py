from django.contrib import admin

from campaigns.models import Campaign
# Register your models here.

class CampaignAdmin(admin.ModelAdmin):
    list_display=('title','public','url')
    search_fields = ['title']
    list_filter=['public']

admin.site.register(Campaign,CampaignAdmin)
