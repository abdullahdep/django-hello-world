from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return [
            'home',
            'about',
            'contact',
            'privacy_policy',
            'terms_and_conditions',
            # Add other named URLs here
        ]

    def location(self, item):
        return reverse(item)