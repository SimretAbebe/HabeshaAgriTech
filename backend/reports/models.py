from django.db import models
from django.conf import settings

class Report(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
