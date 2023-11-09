
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


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
  #  email = models.EmailField(blank=True, unique=True)
    # email = User.email
    # firstname = models.CharField(max_length=70)
    # lastname = models.CharField(max_length=70)
    
    profile_pic = models.ImageField(default='default.png', upload_to='profile_pics')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    gpa = models.FloatField(default=0)
    documents = models.FileField(upload_to='documents')
    skill = models.CharField(max_length=255)
    course=models.CharField(max_length=255)
    biography=models.CharField(max_length=500)
    labname=models.CharField(max_length=255)

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

    # Splits Student Profile tags with comma for display in profile page
    def skill_list(self):
        return self.skill.split(',')
    
    # Splits Student Profile courses with comma for display in profile page
    def course_list(self):
        return self.course.split(',')
    
    def __str__(self):
        return f'{self.user.username} StudentProfile'

    # These two properties will check if the user is a lab or student
    @property
    def is_student(self):
        return self.groups.filter(name='student').exists()
    
    @property
    def is_lab(self):
        return self.groups.filter(name='lab').exists()


# class Mentor(models.Model):
#     user2 = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     biography = models.TextField()
#     profile_pic = models.ImageField(default='default.png', upload_to='profile_pics')
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     documents = models.FileField(upload_to='documents')
#     labname=models.CharField(max_length=255)
#     skill = models.CharField(max_length=255)
#     requiredcourse=models.CharField(max_length=255)
#     # def __str__(self):
#     #     return self.objects

