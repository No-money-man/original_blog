from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'created_datetime', 'updated_datetime')
    list_display_links=('id', 'title')
    # list_display = forms.CharField(widget=CKEditorWidget())

admin.site.register(Blog, BlogAdmin)
