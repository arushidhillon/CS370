from django.db import models
from django.db import models


<<<<<<< HEAD
class Skill(models.Model):
  #firstname = models.CharField(max_length=255)
  #lastname = models.CharField(max_length=255)
  skill=models.CharField(max_length=255)
  
  def __str__(self):
		  return self.skill

class Skills(models.Model):
  skill = models.CharField(max_length=100)

=======
class User(models.Model):
    username = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
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
    subject =  models.CharField(max_length=4,choices =SUBJECT)
    skill = models.CharField(max_length=255)


class Student(User):
    gpa = models.IntegerField(default=0)
    documents = models.IntegerField(default=0)
    def __str__(self):
        return self.student_text

class Mentor(User):
    biography = models.TextField()
    def __str__(self):
        return self.mentor_text
>>>>>>> 30b002d9199936c0a7bff8ceb7ec87c830da5d64
