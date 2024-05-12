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
    path('', views.PostList.as_view(), name='home'),
    # If you had a human resources web app that identified workers by their ID badge number,
    #  then you could use the syntax <int:id_badge> to pass the integer argument to the URL path. Alternatively,
    #   a car mechanics web app identifying cars by their alphanumeric registration plate could do so with <str:reg>
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]