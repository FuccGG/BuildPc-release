# Generated by Django 2.2.6 on 2020-05-22 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component_parts', '0009_playeraction_ssd'),
    ]

    operations = [
        migrations.AddField(
            model_name='playeraction',
            name='user_id',
            field=models.IntegerField(default=1),
        ),
    ]
