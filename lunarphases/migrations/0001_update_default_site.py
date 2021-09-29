from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('sites', '0002_alter_domain_unique'),
    ]

    def forwards_func(apps, schema_editor):
        # We get the model from the versioned app registry;
        # if we directly import it, it'll be the wrong version
        Site = apps.get_model("sites", "Site")
        default_site_id = 1
        default_site_domain = 'calendariolunar.cl'

        default_site = Site.objects.get_or_create(
            id=default_site_id,
            domain=default_site_domain,
            name=default_site_domain,
        )

    def reverse_func(apps, schema_editor):
        pass

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]