from django.db import models

<<<<<<< HEAD
class Skill(models.Model):
  #firstname = models.CharField(max_length=255)
  #lastname = models.CharField(max_length=255)
  skill=models.CharField(max_length=255)
  
  def __str__(self):
		  return self.skill
=======
class Skills(models.Model):
  skill = models.CharField(max_length=100)
>>>>>>> 1d91ccb14ba3b661f77659dcf7ff672f718cbb44
