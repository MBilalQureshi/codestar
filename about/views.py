from django.shortcuts import render, get_object_or_404
from .models import About

def about_me_detail(request):
    queryset = About.objects.order_by('-updated_on').first()

    return render(
        request,
        'blog/about_me.html',
        {"about_me":queryset}
    )
