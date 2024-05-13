from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# admin.site.register(Post)

'''
Note: The decorator is how we register a class, compared to just registering the standard model as we did before. When we use a class,
we register it with a decorator that is more Pythonic and allows us to customise how the models we are registering will appear on the admin site.
'''
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('title', 'slug', 'status','created_on')
    search_fields = ['title']
    list_filter = ('status','created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Comment)