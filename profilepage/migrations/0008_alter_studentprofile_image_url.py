# Generated by Django 4.2.5 on 2023-12-04 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0007_alter_studentprofile_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='image_url',
            field=models.TextField(blank=True, default='https://static.thenounproject.com/png/5034901-200.png', max_length=500, null=True),
        ),
    ]
