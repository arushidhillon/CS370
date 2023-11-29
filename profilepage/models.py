
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


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
    matches = models.ManyToManyField("self", related_name='matched_by', symmetrical=False, blank=True)
    picture_name=models.CharField(default="none", max_length=255)
    profile_pic = models.ImageField(default='default.png', upload_to='profile_pics')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    gpa = models.FloatField(default=0)
    document_name=models.CharField(default="none", max_length=255)
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
    
    def get_fname(self):
        return self.user.first_name


    def __str__(self):
        return f'{self.user.username} StudentProfile'

    # These two properties will check if the user is a lab or student
    @property
    def is_student(self):
        return self.user.groups.filter(name='student').exists()
    
    @property
    def is_lab(self):
        return self.user.groups.filter(name='lab').exists()
    
    #These functions get the user's information from Django's User model.
    def get_user_name(self):
        return self.user.email.split('@')[0]
    def get_first_name(self):
        return self.user.first_name
    def get_last_name(self):
        return self.user.last_name
    def get_email(self):
        return self.user.email



# Create a new group
student_group = Group(name='student')
student_group.save()
lab_group = Group(name='lab')
lab_group.save()

# class Matched(models.Model):
#     follower = models.CharField(max_length=100)
#     user = models.CharField(max_length=100)

#     def __str__(self):
#         return self.user
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

