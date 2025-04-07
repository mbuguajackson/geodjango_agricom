# Generated by Django 5.1 on 2025-04-07 05:21

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField()),
                ('area', models.FloatField()),
                ('perimeter', models.FloatField()),
                ('county3_field', models.FloatField()),
                ('county3_id', models.FloatField()),
                ('county', models.CharField(max_length=20)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
