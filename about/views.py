from django.shortcuts import render, get_object_or_404
from .models import About
from django.contrib import messages
from .forms import CollaborateForm

def about_me(request):
    about = About.objects.order_by('-updated_on').first()
    
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Collaboration request received! I endeavour to respond within 2 working days.'
        )
    collaborate_form = CollaborateForm()

    return render(
        request,
        'about/about.html',
        {"about":about,"collaborate_form":collaborate_form,}
    )
