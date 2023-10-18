from django.db import models

class Skills(models.Model):
  skill = models.CharField(max_length=100)
