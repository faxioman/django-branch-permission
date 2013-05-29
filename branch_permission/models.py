from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class ModelPermission(models.Model):
    owner = models.ForeignKey(User)
    sites = models.ManyToManyField(Site, null=True, blank=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        abstract = True