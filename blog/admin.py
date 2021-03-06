from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status','created_on', 'updated_on', 'published_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)