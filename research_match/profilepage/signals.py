from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import StudentProfile

# This function creates profile for each new user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(user=instance)

#This function saves the profile every time user saves it
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.StudentProfile.save()
        