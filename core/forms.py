from django import forms
from django.contrib.auth.models import User
from .models import Profile, Journal, Comment
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _


class JournalForm(forms.Form):
    Your_Movie_Titles = forms.CharField
    image = forms.ImageField()
    About_this_movie = forms.CharField(widget=forms.Textarea)
    Your_Appreciation_or_Critics_about_this_movie = forms.CharField()



class JournalModelForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['image', 'Your_Movie_Title', 'Your_Appreciation_or_Critics_about_this_movie', 'About_this_movie']



class SignUpForm(UserCreationForm):
            
    username = forms.CharField(label=_("Username"), widget=forms.TextInput)
    
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
        
    class Meta:
        model = User
        fields = (
                'username',
                'first_name',
                'last_name',
                'email',
        #       'birth_date',
        #       'your_referral',
                'password1',
                'password2',
                )       

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = user.first_name
        user.last_name = user.last_name
        user.email = user.email

        if commit:
                 user.save()
                
        return user


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image', 'about_me', 'location', 'passion', 'plan']


class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    #parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(label='',widget=forms.Textarea)


