from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post

class TestBlogViews(TestCase):

    def setUp(self):
        # Self represents within our tests. self references the current class instance. It is used to create and access variables that belong to that class.
        # In the context of testing, especially with Django's TestCase class, self is used in the setUp method to create instance variables you want to use across
        #  different test methods. And then, inside our test methods, we can access these variables to run our tests.
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post(title="Blog title", author=self.user,
                         slug="blog-title", excerpt="Blog excerpt",
                         content="Blog content", status=1)
        self.post.save()

    def test_render_post_detail_page_with_comment_form(self):
    # There are several steps to this code:
    # In the test method, we use reverse to generate a URL for accessing the post_detail view, providing 'blog-title' as an argument.
    # This 'blog-title' is the slug for the blog post, which we previously created as self.post during the setUp method.
    # Then, we use self.client.get() with this URL to send a GET request to the post_detail view.
    # The response from the view is then captured in the response variable.
    # When we print response.content to the terminal, we see the full HTML that the browser would use to build that page. We can see both the <head> and <body> content are contained within response.content. This enables us to run tests on it to confirm that the page would be rendered as expected, such as.
    # self.assertIn(b"Blog title", response.content)
    # When we print response.context to the terminal, we see the context object that is passed to the template from the relevant view. This includes our own custom context, such as 'comment_count' and 'comment_form', as well as many other context variables automatically created by Django. This also enables us to run tests on response.context to confirm that the correct objects were passed to the template by the view.
    # The assertIsInstance assertion in:
    # self.assertIsInstance(
    #     response.context['comment_form'], CommentForm)
    # Verifies that the comment_form from the post_detail view's context is an instance of the CommentForm class.
    # GETting a view response
    # As we know, our view returns different things depending on if the request method used is GET or POST. To access the response that our view would return to a GET request, the self.client.get() method is used, with the reverse method passed in to generate the relevant URL with the provided view arguments.

    # response = self.client.get(
    #     reverse('post_detail',args=['blog-title']))
    # Note: You only need to provide a value for args if the URL you are building in reverse expects them. You can check what your URLs expect in the urls.py file.

    # The response returned by the get() method then contains all the information we can run our tests on, including the HTML content and the context.
        response = self.client.get(reverse(
            'post_detail', args=['blog-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)
    
    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        # Commenting on a blog post is reserved for authenticated users, so a user must log in before commenting. We use the username and password previously defined in the setUp method to test this step.
        self.client.login(username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(
            reverse('post_detail', args=['blog-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Comment submitted and awaiting approval',
                      response.content)

    def test_successful_collaboration_request_submission(self):
        """Test for a user requesting a collaboration"""
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.', response.content)