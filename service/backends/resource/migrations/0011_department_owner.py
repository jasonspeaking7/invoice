# Generated by Django 2.1 on 2018-08-21 06:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resource', '0010_auto_20180821_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='owner',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
