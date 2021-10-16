from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()

class Books(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.IntegerField()

    class Meta:
        ordering = ['-id', ]
    
    @property
    def rating(self):
        ratings = self.ratings.all()
        if ratings:
            sum_ = 0
            for rating in ratings:
                sum_ += rating.value
            return round(sum_ / len(ratings), 2)
        return 0


class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    books = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='ratings')
    value = models.IntegerField(validators=[
                                MaxValueValidator(5),
                                MinValueValidator(1)
                                ])
    
    def __str__(self):
        return f'This is your books {self.title}'
