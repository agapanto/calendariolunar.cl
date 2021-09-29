import datetime
from django.contrib.sitemaps import Sitemap
from django.utils.translation import gettext as _
from django.urls import reverse


class CalendarioLunarSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
    i18n = True

    def items(self):
        today = datetime.datetime.now().date()

        return [
            {
                'url': 'current_lunar_phase',
                'kwargs': {}
            },
            {
                'url': 'following_lunar_phases',
                'kwargs': {}
            },
            {
                'url': 'monthly_calendar',
                'kwargs': {
                    'year': today.year,
                    'month': today.month,
                }
            },
            {
                'url': 'specific_lunar_phase',
                'kwargs': {
                    'year': today.year,
                    'month': today.month,
                    'day': today.day,
                }
            }
        ]

    def location(self, item):
        return reverse(
            item['url'],
            kwargs=item['kwargs']
        )