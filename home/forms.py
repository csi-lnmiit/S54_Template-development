from django import forms
from accounts.models import *

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('last_name','age')
		widgets = {
			'last_name' : forms.TextInput(
				attrs = {'class' : 'form-control'}
				),
			'age' : forms.TextInput(
				attrs = {'class' : 'form-control'}
				),
		}
