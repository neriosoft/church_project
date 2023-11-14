from django.contrib.sitemaps import Sitemap
from .models import Event


class EventSitemap(Sitemap):
    def items(self):
        return Event.objects.all()
