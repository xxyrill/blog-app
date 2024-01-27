from django.db import models

# this is for importing the db models

from django.urls import reverse # new

# The reverse function in Django is used to generate URLs for
# a given view or a named URL pattern. It is particularly useful when you
# want to dynamically create URLs in your views, templates, or tests without
# hardcoding them.
# gi add nmu ni nga line of code para maka post ka ug blog post

# imported django db models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    # gi add nmu ni nga line of code para maka post ka ug blog post