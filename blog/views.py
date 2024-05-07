from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Generic views are beneficial for dealing with repetitive full-stack coding tasks such as displaying database contents to a webpage.
# It handles the most common use cases in web app development.
# These views allow us to create pages of blog posts, products, orders, or anything else that would be in a list, very quickly.
# The generic views do a lot of things automatically without requiring a lot of time and effort from the developer. The downside is that
# they offer limited customisation. If you want something that goes beyond what the generic views offer, you may be better off using a standard
# Django view and writing it yourself.


# Only by entering "model = Post" one can see all the data in view not template,you do not need to add the HTML template name or list 
# which posts you want to see. Let’s add these optional lines of code in the PostView class,
# we are still going to remove model = Post and add queryset = Post.objects.all() and template_name = "post_list.html", result is still same on view
class PostList(generic.ListView):
    # 1
    # The generic view very cleverly infers the template name itself. By which, we mean that it follows a certain rule to decide what the template should be called.
    # As shown in the example above, the post part of the name refers to the model and the list part is the type of generic view we're using. So,
    # Django expects there to be a template called post_list.html. even if you don't write template_name = "post_list.html"
    # model = Post
    
    # 2
    # queryset = Post.objects.all() is same as model = Post BUT to apply filter use queryset = Post.objects...
    # queryset = Post.objects.all()


    #     A filter works just like the filter on your coffee machine. It stops certain things from getting through - coffee grounds, for example. It only allows through the things that we want, such as, delicious coffee.

    # In the code, we asked Django only to allow posts with the author field set to 1 through the filter. Everything else was filtered out. Filters are a powerful way for us to perform queries on our database.

    # Another method that we can use is order_by. This method allows us to specify the ordering of our records. If we wanted to display all of our posts ordered from the earliest date to the most recent, we could do this:

    # class PostList(generic.ListView):
    #     queryset = Post.objects.all().order_by("created_on")
    # To reverse the order, put a minus sign in front of the field name. So, to order in descending order - from most recent to earliest, which is the most sensible way of ordering blog posts, we would use:

    # class PostList(generic.ListView):
    #     queryset = Post.objects.all().order_by("-created_on")
    # The ordering works with filters too!

    # queryset = Post.objects.filter(author=3)
    # queryset = Post.objects.filter(status=1).order_by("-created_on")
    # template_name = "post_list.html"

    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )