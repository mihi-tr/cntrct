from campaigns.models import Campaign
from django import forms

class AddFromURLForm(forms.Form):
    url = forms.URLField()

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['title','url','image_url','overview']
