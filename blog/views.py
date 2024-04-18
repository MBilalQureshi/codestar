from django.shortcuts import render
from django.views import generic
from .models import Post

# Generic views are beneficial for dealing with repetitive full-stack coding tasks such as displaying database contents to a webpage.
# It handles the most common use cases in web app development. 
# Only by entering "model = Post" one can see all the data in view not template,you do not need to add the HTML template name or list 
# which posts you want to see. Let’s add these optional lines of code in the PostView class,
# we are still going to remove model = Post and add queryset = Post.objects.all() and template_name = "post_list.html", result is still same on view
class PostList(generic.ListView):
    # 1
    # model = Post
    
    # 2
    queryset = Post.objects.all()
    template_name = "post_list.html"