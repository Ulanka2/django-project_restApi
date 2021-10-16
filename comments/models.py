from django.db import models
from tasks.models import Books
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    books = models.ForeignKey(Books, on_delete=models.SET_NULL,null=True, related_name='comments')
    content = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)


