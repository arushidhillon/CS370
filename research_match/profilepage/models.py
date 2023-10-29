from django.db import models

class Skill(models.Model):
  #firstname = models.CharField(max_length=255)
  #lastname = models.CharField(max_length=255)
  skill=models.CharField(max_length=255)
  
  def __str__(self):
		  return self.skill
