from django.db import models
from django.utils import timezone

class Blog(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    blog_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
