# Generated by Django 2.2.6 on 2020-01-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component_parts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='motherboard',
            name='slot_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
