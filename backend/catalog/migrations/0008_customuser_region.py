# Generated by Django 2.2.dev20180523150237 on 2018-08-11 20:12

from django.db import migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20180810_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='region',
            field=mptt.fields.TreeManyToManyField(blank=True, related_name='user_region', to='catalog.Region'),
        ),
    ]
