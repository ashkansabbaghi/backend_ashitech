from django.contrib import admin
from .models import Blog, ImageBlog, Tag
# from auth.models import CustomUser


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'caption_limit', 'slug',
                    'status', 'publish', 'created', 'updated')

    def caption_limit(self, obj):
        return obj.caption[:30]+'...'


admin.site.register(Tag)
admin.site.register(ImageBlog)