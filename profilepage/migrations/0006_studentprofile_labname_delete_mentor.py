# Generated by Django 4.2.5 on 2023-11-08 02:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("profilepage", "0005_rename_user_mentor_user2"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentprofile",
            name="labname",
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="Mentor",
        ),
    ]