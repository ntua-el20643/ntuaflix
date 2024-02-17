# Generated by Django 5.0.1 on 2024-02-05 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_crews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentTconst', models.CharField(blank=True, max_length=255, null=True)),
                ('seasonNumber', models.PositiveIntegerField(blank=True, null=True)),
                ('episodeNumber', models.PositiveIntegerField(blank=True, null=True)),
                ('tconst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.movies')),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('averageRating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('seasonNumber', models.PositiveIntegerField()),
                ('tconst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.movies')),
            ],
        ),
    ]