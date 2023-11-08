# Generated by Django 4.2.5 on 2023-10-30 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=70)),
                ("email", models.CharField(max_length=70)),
                ("firstname", models.CharField(max_length=70)),
                ("lastname", models.CharField(max_length=70)),
                (
                    "background",
                    models.CharField(
                        choices=[("S", "Student"), ("M", "Mentor")], max_length=1
                    ),
                ),
                (
                    "subject",
                    models.CharField(
                        choices=[
                            ("BIOL", "Biology"),
                            ("CHEM", "Chemistry"),
                            ("PHYS", "Physics"),
                            ("MATH", "Mathematics"),
                            ("COMP", "Computer Science"),
                            ("PSYC", "Psychology"),
                            ("HIST", "History"),
                            ("OTHE", "Other"),
                        ],
                        max_length=4,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Mentor",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="profilepage.user",
                    ),
                ),
                ("biography", models.TextField()),
            ],
            bases=("profilepage.user",),
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="profilepage.user",
                    ),
                ),
                ("gpa", models.IntegerField(default=0)),
                ("documents", models.IntegerField(default=0)),
                ("skill", models.CharField(max_length=255)),
            ],
            bases=("profilepage.user",),
        ),
    ]