from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from campaigns.models import Campaign
import changeorg

corg = changeorg.Client(api_key=settings.CHANGEORG_API_KEY)

class Command(BaseCommand):
    args=""
    help="Updates the local campaigns from change.org"

    def handle(self,*args, **options):
        c = Campaign.objects.filter(change_id__isnull=False)
        ids = [str(i.change_id) for i in c]
        petitions=corg.get_petitions(ids)['petitions']
        for pd in petitions:
            # print pd.keys()
            p = c.get(change_id = pd['petition_id'])
            p.overview = pd['overview']
            p.title = pd['title']
            p.image_url = pd['image_url']
            p.signature_count = pd['signature_count']
            p.save()

            

