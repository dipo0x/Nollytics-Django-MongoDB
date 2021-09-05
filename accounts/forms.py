from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _


				 
class EditProfileForm(UserChangeForm):
	class meta:
		model = User
		fields = (
				'email',
				'password',
				'first_name',
				'last_name',
				
		 )	




class ImageUploadForm(forms.Form):
    image = forms.ImageField()
		 


		 
