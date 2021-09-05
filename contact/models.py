from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model)	:
	user = models.ForeignKey(User, default=7, null=False, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=80)
	number = models.IntegerField()
	message = models.TextField()


	def __str__ (self):
		return self.email		



