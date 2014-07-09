from django.db import models

# Create your models here.

class Campaign(models.Model):
    change_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=512)
    url = models.URLField(unique=True)
    overview = models.TextField()
    signature_count = models.IntegerField(default=0)
    image_url = models.URLField()
    public = models.BooleanField(default=False)
