from django.views.generic import ListView, DetailView
# imported the ListView and DetailView class from django

from django.views.generic.edit import CreateView, UpdateView, DeleteView # new

from django.urls import reverse_lazy # new

from .models import Post

# refers to the models.py in the current app, then import class Post in models.py

class BlogListView(ListView):
    model = Post    # refers to the Post model in models.py, the class will interact with the Post model
    template_name = 'home.html'     # refers to the home.html in templates

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

# l7, created a new class and used ListView as a subclass. The class will inherit
# the attributes of the class ListView (such as  simplifying the process of
# displaying a list of objects retrieved from a database model)

# l8, specifies the Django model (Post in this case) from which the list of objects
# should be retrieved. The ListView will automatically query the database for
# all instances of the specified model.

# l9, indicates the template that should be used to render the list of objects.
# In this case, the template is named 'home.html'. The template will have access
# to the list of objects through a context variable.

# ***

# By using ListView as a subclass, you don't have to write the view logic to retrieve
# objects from the database, paginate the results, and pass them to a template.
# The class-based view (BlogListView) takes care of these common tasks for you.
#
# Here's a brief explanation of the key functionalities provided by ListView:
#
# Object Retrieval: ListView automatically retrieves a list of objects from the
# specified model (Post in this case).
#
# Pagination: If there are many objects, ListView handles pagination automatically.
#
# Context Data: The list of objects is automatically included in the context data
# sent to the template.
#
# By subclassing ListView, you adhere to the DRY (Don't Repeat Yourself) principle,
# as Django abstracts away the common patterns for displaying lists of objects. It
# promotes code reuse and makes your codebase more maintainable.