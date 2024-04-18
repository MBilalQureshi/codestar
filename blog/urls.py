from . import views
from django.urls import path

'''
URL naming
The best URLs are clearly named and can almost be guessed by your user. So, choose a structure that makes sense for your project.
Your About Me page may live at the about/ URL, whereas logging into your site may live at accounts/login/.

Although it may be tempting, it is best not to give your URLs the same name as your view function or vice versa.
So, our blog/ URL would not call a view function named blog. That's because if we do need to change our URLs later on, or have more
than one URL pointing to the same view function then the naming can quickly get out of sync.

As the Django documentation says, tying URLs to Python function names is a Bad And Ugly Thing.
'''

urlpatterns = [
    # As the view is a class, you need an as_view() method
    path('posts/', views.PostList.as_view(), name='home'),
]