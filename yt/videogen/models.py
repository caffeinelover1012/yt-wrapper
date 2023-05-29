from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    generated_script = models.TextField()
    tags = models.CharField(max_length=200)
    date_generated = models.DateTimeField(auto_now_add=True)
