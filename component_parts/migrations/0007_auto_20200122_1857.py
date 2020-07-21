# Generated by Django 2.2.6 on 2020-01-22 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('component_parts', '0006_auto_20200120_0155'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount_of_memory', models.IntegerField()),
                ('interface', models.CharField(max_length=100)),
                ('power', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='ssd',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='component_parts.SSD'),
        ),
    ]