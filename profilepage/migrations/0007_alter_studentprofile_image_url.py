# Generated by Django 4.2.5 on 2023-12-01 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0006_studentprofile_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='image_url',
            field=models.URLField(blank=True, default='https://static.thenounproject.com/png/5034901-200.png', null=True),
        ),
    ]
