# Generated by Django 4.2.5 on 2023-11-28 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0004_studentprofile_document_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='matches',
            field=models.ManyToManyField(blank=True, related_name='matched_by', to='profilepage.studentprofile'),
        ),
    ]
