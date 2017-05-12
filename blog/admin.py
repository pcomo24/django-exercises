from django.contrib import admin
from blog.models import Blog, Post, Poll, Choice, Tag, Category

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'blog')
@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'slug')
    filter_horizontal = ('categories',)
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('answer', 'vote_count')
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
