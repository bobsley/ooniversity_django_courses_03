# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10, choices=[(b'M', b'Male'), (b'F', b'Femail')])),
                ('phone', models.CharField(max_length=25, null=True, blank=True)),
                ('address', models.CharField(max_length=255, null=True, blank=True)),
                ('skype', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_staff', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
