from django.contrib import admin

from accounts.models import Post
from django.contrib import admin

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Your_name', 'Your_Post_title', 'Your_Post', 'id']}),
    ]


admin.site.register(Post, PostAdmin)



admin.site.site_header = 'Nollytics'
