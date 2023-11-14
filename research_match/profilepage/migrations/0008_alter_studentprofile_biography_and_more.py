# Generated by Django 4.2.5 on 2023-11-08 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profilepage", "0007_alter_studentprofile_gpa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentprofile",
            name="biography",
            field=models.CharField(blank="True", max_length=500),
        ),
        migrations.AlterField(
            model_name="studentprofile",
            name="course",
            field=models.CharField(blank="True", max_length=255),
        ),
        migrations.AlterField(
            model_name="studentprofile",
            name="gpa",
            field=models.FloatField(blank="True", default=0),
        ),
        migrations.AlterField(
            model_name="studentprofile",
            name="skill",
            field=models.CharField(blank="True", max_length=255),
        ),
    ]