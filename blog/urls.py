from django.urls import path

# imports the path from django url module

from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

# referenced to all the class modules in views.py

urlpatterns = [
    path('post/<int:pk>/edit/', BlogDeleteView.as_view(), name='post_delete'),   # url path to blog delete view
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),   # url path to blog update view
    path('post/new/', BlogCreateView.as_view(), name='post_new'),   # url path to blog create view
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),   # url path to blog detail view
    path('', BlogListView.as_view(), name='home'),  # url path to blog list view

]