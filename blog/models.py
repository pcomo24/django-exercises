from django.db import models
from django.conf import settings

class Blog(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=140, blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

class Poll(models.Model):
    question = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.question

class Choice(models.Model):
    answer = models.CharField(max_length=50)
    vote_count = models.IntegerField(default=0)
    poll = models.ForeignKey(Poll)

    def __str__(self):
        return self.answer
