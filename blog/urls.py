from . import views
from django.urls import path

urlpatterns = [
    # As the view is a class, you need an as_view() method
    path('', views.PostList.as_view(), name='home'),
]