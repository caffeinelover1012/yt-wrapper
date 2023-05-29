from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_of_generation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
