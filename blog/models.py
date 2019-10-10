from django.conf import settings
from django.db import models


class Post(models.Model):
    """
    Stores posts for the blog
    """
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),

    ]



    title = models.CharField(max_length=255,help_text='The test of the content')
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "Published" to make pubblic'
    )
    slug = models.SlugField(
        null=True,
        unique_for_date='published',
    )
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text = 'The publishing date'
    )
    
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.PROTECT,
        related_name = 'blog_posts',
        null = True,
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    
