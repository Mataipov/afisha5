# Generated by Django 3.2.16 on 2022-12-04 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(blank=True, default=30, null=True),
        ),
    ]
