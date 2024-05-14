# Why might you override the model method in a Django class-based view with a queryset? For example:

# Before
# model = Post
# template_name = "post_list.html"

# After
# queryset = Post.objects.filter(status=1)
# template_name = "post_list.html"

# # To allow extra filtering of the data for the template.
# Answer
# Correct:Yes, queryset allows extra data filtering before sending data in the context to the template. Well done!

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

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
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts. 
    **Context**

    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        Number of posts per page.
        
    **Template:**

    :template:`blog/index.html`
    """
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
    # The slug parameter gets the argument value from the URL pattern named post_detail
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    # when we use post.comments.all(), it will return all comments related to the selected post by using related_name="comments".
    # This is what is called a reverse lookup. We don't access the Comment model directly. Instead, we fetch the related data from the perspective of the Post model.
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    # we test this POST now see test_views.py
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Calling the save method with commit=False returns an object that hasn't yet been saved to the database so that we can modify it further. We do this because we need to populate the post and author fields before we save. The object will not be written to the database until we call the save method again.
    # You can think of the commit=False argument like git commits. When using git, we can use git add to add new and updated files and to remove files. These changes are not finalised until we use git commit.

    # In the same way, calling the comment_form.save method with commit=False, allows us to make changes to the database record until we call the save method with no arguments, which commits our changes to the database.
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted and awaiting approval'
        )
    # Outside the if statement, we create a blank instance of the CommentForm class. This line resets the content of the form to blank so that a user can write a second comment if they wish.
    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "coder": "Muhammad Bilal",
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        # By specifying instance=comment, any changes made to the form will be applied to the existing Comment, instead of creating a new one.
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')
    # HttpResponseRedirect is a Django class that tells the browser to go to a different URL.
    # reverse is a Django function that constructs a URL from the provided URL path name and any relevant URL arguments: args=[slug].
    # Using the slug argument ensures the user is returned to the same blog post on which they edited or deleted a comment.
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    # HttpResponseRedirect is a Django class that tells the browser to go to a different URL.
    # reverse is a Django function that constructs a URL from the provided URL path name and any relevant URL arguments: args=[slug].
    # Using the slug argument ensures the user is returned to the same blog post on which they edited or deleted a comment.
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))