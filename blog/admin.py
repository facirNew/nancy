from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'time_create', 'is_published', 'get_tags')
    list_display_links = ('title', 'photo')
    search_fields = ('title', 'content')
    list_editable = ('is_published', )
    list_filter = ('tags', 'time_create')
    prepopulated_fields = {'slug': ('title', )}

    @staticmethod
    def get_tags(obj):
        return [tag.name for tag in obj.tags.all()]


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


# class BlogTagsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'post', 'tag')
#     list_display_links = ('id', 'post', 'tag')
#     search_fields = ('post', 'tag')


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tags, TagsAdmin)
# admin.site.register(BlogTags, BlogTagsAdmin)


