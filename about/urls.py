from django.urls import path
from . import views

urlpatterns = [
    path('childabout',views.about_me_detail,name='about'),
]