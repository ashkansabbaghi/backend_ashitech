from django.contrib import admin
from .models import Profile ,specialty
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# admin.site.register(Profile)
@admin.register(Profile)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('user','mobile','bio_limit')

    def bio_limit(self, obj):
        return obj.bio[:90]+'...'

admin.site.register(specialty)