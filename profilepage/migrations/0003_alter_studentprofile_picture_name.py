# Generated by Django 4.2.5 on 2023-11-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profilepage", "0002_studentprofile_picture_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentprofile",
            name="picture_name",
            field=models.CharField(default="none", max_length=255),
        ),
    ]