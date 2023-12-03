from django.db import models
from django.conf import settings
from django.utils import timezone

class SearchQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='search_queries')
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} searched for '{self.query}' at {self.timestamp}"

