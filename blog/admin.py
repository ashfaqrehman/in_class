from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    

    prepopulated_fields = {'slug': ('name',)}



class PostAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'created',
        'updated',
    )

    list_filter = (
        'status',
        'topics',
    )
    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )
    prepopulated_fields = {
        'slug':('title',)
    }

admin.site.register(models.Post, PostAdmin)
