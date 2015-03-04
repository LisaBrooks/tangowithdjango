from django import forms 
from django.contrib.auth.models import User
from Bao.models import UProfile 

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model= User
		fields=('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model=UProfile
		fields=('picture', 'score')	
		#score=forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'readonly'}))	
