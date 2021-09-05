from post.models import Post
from django import forms
from post.models import Post
from post.models import Celebs
from post.models import Comment

class PostForm(forms.ModelForm):
	

    class Meta:
        model = Post
        exclude = ['pub_date', 'slug']

class CelebsForm(forms.ModelForm):
	

    class Meta:
        model = Celebs
        exclude = ['pub_date', 'id']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['created_on']
        fields = ['your_name', 'body']
        
