# Generated by Django 3.2 on 2022-04-20 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meats',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
