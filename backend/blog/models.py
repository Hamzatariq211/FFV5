from django.db import models

class Blog(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    blog_data = models.TextField()

    def __str__(self):
        return self.title
