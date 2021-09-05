from post.models import Post
from post.models import Celebs
from post.models import Comment
from django.contrib import admin



from django.contrib import admin

from post.models import Post, Comment





class PostAdmin(admin.ModelAdmin):

    list_display = ('Your_name', 'Your_Post_title', 'Your_Post', 'Image', 'id', 'Your_Appreciation_or_Critics_about_this_movie', 'pub_date')


    search_fields = ['Your_name']

    prepopulated_fields = {'id': ('Your_Post_title',)}

  

admin.site.register(Post, PostAdmin)





# PostAdmin)

#

#

# PostAdmin)


#


#


#class CommentAdmin(admin.ModelAdmin):


#    list_display = ('name', 'body', 'post', 'created_on', 'active')


#    list_filter = ('active', 'created_on')


#    search_fields = ('name', 'email', 'body')


#    actions = ['approve_comments']


#


#    def approve_comments(self, request, queryset):


#        queryset.update(active=True)



#class PostAdmin(admin.ModelAdmin):
#	exclude : ('slug')
#	prepopulated_fields = {'id': ('Your_Post_title',)}
#	fieldsets = [
#        (None,               {'fields': ['Your_name', 'Your_Post_title', 'Your_Post', 'Image', 'id', 'Your_Appreciation_or_Critics_about_this_movie']})
#    ]


#admin.site.register(Post, PostAdmin)

class CelebsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Your_name', 'Your_Post_title', 'Your_Post', 'Image']}),
    ]


admin.site.register(Celebs, CelebsAdmin)


class CommentAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['your_name', 'post', 'body']})
   ]


admin.site.register(Comment)