# Generated by Django 4.2.6 on 2023-11-14 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0003_alter_studentprofile_matches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='matches',
            field=models.ManyToManyField(blank=True, related_name='matched_by', to='profilepage.studentprofile'),
        ),
    ]
