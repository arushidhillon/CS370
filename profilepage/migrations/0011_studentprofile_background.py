# Generated by Django 4.2.5 on 2023-12-06 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0010_remove_studentprofile_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='background',
            field=models.CharField(choices=[('S', 'Student'), ('M', 'Mentor')], default='S', max_length=1),
            preserve_default=False,
        ),
    ]
