from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.contrib.auth.models import User # Import the built-in User model, which is a sender
from django.dispatch import receiver # Import the receiver
from .models import StudentProfile

# this function automatically creates a profile when a user registers.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(user=instance)

# This function saves the newly created profile.
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.studentprofile.save()