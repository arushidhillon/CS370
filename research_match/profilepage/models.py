
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db.models.signals import post_save


# class Skill(models.Model):
#   #firstname = models.CharField(max_length=255)
#   #lastname = models.CharField(max_length=255)
#   skill=models.CharField(max_length=255)
  
#   def __str__(self):
# 		  return self.skill

# class Skills(models.Model):
#   skill = models.CharField(max_length=100)


    
class StudentProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, default='', unique=True)
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)

    profile_pic = models.ImageField(default='default.png', upload_to='profile_pics')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    gpa = models.IntegerField(default=0)
    documents = models.IntegerField(default=0)
    skill = models.CharField(max_length=255)
    course=models.CharField(max_length=255)
    biography=models.CharField(max_length=500)

    BACKGROUND = [
        ("S","Student"),
        ("M","Mentor")
    ]
    background = models.CharField(max_length=1, choices=BACKGROUND)
    SUBJECT = [
        ("BIOL", "Biology"),
        ("CHEM", "Chemistry"),
        ("PHYS", "Physics"),
        ("MATH", "Mathematics"),
        ("COMP", "Computer Science"),
        ("PSYC", "Psychology"),
        ("HIST", "History"),
        ("OTHE", "Other")
    ] 

    def __str__(self):
        return f'{self.user.username} StudentProfile'
    
# Create Profile when New User signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = StudentProfile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)


class Mentor(models.Model):
    biography = models.TextField()
    # def __str__(self):
    #     return self.objects

