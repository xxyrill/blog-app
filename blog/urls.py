from django.urls import path

# referenced to the path in blog_project\urls.py

from .views import BlogListView, BlogDetailView # new

# referenced to the views module and import the BlogListView class from django

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # new
    path('', BlogListView.as_view(), name='home'),

]