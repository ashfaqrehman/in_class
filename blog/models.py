from django.conf import settings
from django.db import models
from django.utils import timezone



class Topic(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=self.model.PUBLISHED)
    def drafts(self):
         return self.filter(status=self.model.DRAFT)
# class PostQuerySet(models.QuerySet):
#     def published(self):
#         return self.filter(status=self.model.PUBLISHED)
#     def drafts(self):
#         return self.filter(status=self.model.DRAFT)




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
        null=False,
        unique_for_date='published',
    )
    
    topics = models.ManyToManyField(
        Topic,
        related_name='blog_posts'
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
        null = False,
    )

    objects = PostQuerySet.as_manager()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def publish(self):
        self.status = self.PUBLISHED
        self.published = timezone.now()
    
