from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class News(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    img = models.URLField()

