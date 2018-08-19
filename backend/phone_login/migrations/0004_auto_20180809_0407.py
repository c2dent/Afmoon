# Generated by Django 2.2.dev20180523150237 on 2018-08-09 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_login', '0003_remove_phonetoken_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonetoken',
            name='nickname',
            field=models.CharField(blank=True, default='Nickname', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='phonetoken',
            name='phone_number',
            field=models.CharField(default='+79889155078', max_length=16),
        ),
    ]