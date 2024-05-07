from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title','updated_on')
    search_fields = ('title','updated_on')
    list_filter = ('title','updated_on')
    summernote_fields = ('content',)