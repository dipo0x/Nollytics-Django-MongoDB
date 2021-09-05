from django.contrib import admin
from .models import Journal, Comment, UserProfile

# Register your models here.
class JournalAdmin(admin.ModelAdmin):

    list_display = ('Your_Movie_Title', 'About_this_movie', 'image', 'slug', 'Your_Appreciation_or_Critics_about_this_movie', 'timestamp')


    search_fields = ['Your_name']

    prepopulated_fields = {'slug': ('Your_Movie_Title',)}


admin.site.register(UserProfile)
admin.site.register(Journal, JournalAdmin)
admin.site.register(Comment)

