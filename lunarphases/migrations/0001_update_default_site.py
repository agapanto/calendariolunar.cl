import django.contrib.sites.models
from django.conf import settings
from django.contrib.sites.models import Site
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    def forwards_func(apps, schema_editor):
        default_site = Site.objects.get(id=1)
        default_site.domain = default_site.name = 'calendariolunar.cl'
        default_site.save()

    def reverse_func(apps, schema_editor):
        pass

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]