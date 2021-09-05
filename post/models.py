from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
	Your_Post_title = models.CharField(max_length=2000)
	id = models.CharField( max_length=5789, primary_key=True)
	Your_name = models.CharField(max_length=900)
	pub_date = models.DateTimeField('date published', auto_now_add=True)   	
	Your_Post = models.TextField(max_length=909000)
	Image = models.ImageField(blank=False,upload_to='profile_image',null=True)
	post = models.ForeignKey(User, on_delete=models.CASCADE)

	Your_Appreciation_or_Critics_about_this_movie= models.TextField(max_length=200000, null="True")
	def __str__(self):
		return self.Your_Post


class Celebs(models.Model):
    Your_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)   
    Your_Post_title = models.CharField(max_length=200)  
    Your_Post = models.TextField(max_length=2000)
    Image = models.FileField(blank=False,upload_to='profile_images')

    id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.Your_Post


class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	your_name = models.CharField(max_length=42)   
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
   
	def __str__(self):
		return self.body



 
