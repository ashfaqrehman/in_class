from django.db import models

class Post(models.Model):
    """
    Stores posts for the blog
    """
    title = models.CharField(max_length=255,help_text='The test of the content')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    
