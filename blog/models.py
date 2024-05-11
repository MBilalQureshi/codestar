from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # The slug attribute with field type SlugField() also generates a single-line form input type text. It accepts Python string data type.
    # A slug is a short label only containing letters, numbers, underscores or hyphens. You would use one as a semantic URL path rather than an integer or database row ID.
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Adding a Meta class:
        The posts are listed from newest to oldest creation time:
        The ordering option adds metadata to the model about the default order in which the list of posts is displayed.
        The posts are now listed from oldest to newest creation time. The - prefix on created_on indicates the posts are displayed
        in descending order of creation date. If no leading - is used, then the order is ascending, and if a ? prefix is used, then the order is randomised.

        The Meta class provides additional information or metadata about the model. One of its options is ordering,
        which specifies how the records associated with the model are ordered. In this case, we've assigned the ordering option a
        list with a single item, the created_on field. You can list more than one field to order on; e.g. the following would order by created_on
        descending and then by author ascending.
        """
        # ordering = ["-created_on"]
        ordering = ["-created_on", "author"]

    def __str__(self):
        """
        When adding posts up till now, they have appeared in the admin panel as Post object(n), where n is an integer denoting the order of posts being added.
        Now, as per the main image, they are identified in a human-readable manner.
        he __str__() method has changed this post identifier to a string literal. By passing self as an argument to the __str__() method,
        you can use the field values in the f-string.

        We also added a Python magic __str__ method to our Post model. We also call this a dunder method because double underscores surround the name.
        This method gives each post a name that superusers, rather than Python developers, can more easily understand. When we look at posts in the console or
        admin panel, this name helps us figure out which post is which.
        """
        # return f"The title of this post is {self.title}"
        return f"{self.title} | written by {self.author}"

        '''
        Other custom methods:
        You can add other similar methods like this to models to make them do more things, like calculating a user's age from their date of birth field or putting a
        preferred title in front of a name. In the world of web development, this helps keep our data organised and user-friendly.
        '''

class Comment(models.Model):
    # related_name
    # While the Post model doesn't have a field named comments, the related_name in our Comment model sets up a logical link, effectively 
    # creating this association, as you can see in the image and the code.
    
    # when we use post.comments.all(), it will return all comments related to the selected post by using related_name="comments".
    # This is what is called a reverse lookup. We don't access the Comment model directly. Instead, we fetch the related data from the perspective of the Post model.
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"