from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Books(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.IntegerField()

    class Meta:
        ordering = ['-id', ]
    
    def __str__(self):
        return f'This is your books {self.title}'