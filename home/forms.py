from django import forms

class SignUpForm(forms.Form):
	username = forms.CharField(
		required = True,
		label = 'Username',
		max_length = 32,
		widget=forms.TextInput(
			attrs={'placeholder':' Username'},
			),
	)
	email = forms.CharField(
		required = True,
		label = 'Email',
		max_length = 32,
	)
	password1 = forms.CharField(
		required = True,
		label = 'Password1',
		max_length = 32,
		widget = forms.PasswordInput()
	)
	password2 = forms.CharField(
		required = True,
		label = 'Password2',
		max_length = 32,
		widget = forms.PasswordInput()
	)
	first_name = forms.CharField(
		required = True,
		label = 'First_Name',
		max_length = 32,

		)