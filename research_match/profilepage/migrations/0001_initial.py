
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentProfile",
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
                (
                    "profile_pic",
                    models.ImageField(default="default.png", upload_to="profile_pics"),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                ("gpa", models.FloatField(default=0)),
                ("documents", models.FileField(upload_to="documents")),
                ("skill", models.CharField(max_length=255)),
                ("course", models.CharField(max_length=255)),
                ("biography", models.CharField(max_length=500)),
                ("labname", models.CharField(max_length=255)),
                (
                    "background",
                    models.CharField(
                        choices=[("S", "Student"), ("M", "Mentor")], max_length=1
                    ),
                ),
                (
                    "matches",
                    models.ManyToManyField(
                        blank=True,
                        related_name="matched_by",
                        to="profilepage.studentprofile",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
