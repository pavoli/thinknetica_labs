from django.contrib.sitemaps import Sitemap

from .models import Vacancy


class VacancySitemap(Sitemap):

    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Vacancy.objects.all()

    def lastmod(self, obj):
        return obj.publish_date
