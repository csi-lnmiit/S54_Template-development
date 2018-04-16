from django import forms

class SignUpForm(forms.Form):
	email = forms.EmailField(
		required = True,
		label = 'Email',
		max_length = 32,
		widget=forms.TextInput(
			attrs={'placeholder':'Email'},
			),
	)
	password1 = forms.CharField(
		required = True,
		label = 'Password1',
		max_length = 32,
		widget = forms.PasswordInput(
			attrs={'placeholder':'Password'},
			),
	)
	password2 = forms.CharField(
		required = True,
		label = 'Password2',
		max_length = 32,
		widget = forms.PasswordInput(
			attrs={'placeholder':'Confirm Password'},
			),
	)
	first_name = forms.CharField(
		required = True,
		label = 'First_Name',
		max_length = 32,
		widget=forms.TextInput(
			attrs={'placeholder':'First Name'},
			),
		)
	last_name = forms.CharField(
		required = False,
		label = 'Last_Name',
		max_length = 32,
		widget=forms.TextInput(
			attrs={'placeholder':'Last Name'},
			),
		)
	age = forms.IntegerField(
		required = False,
		label = 'Age',
		widget = forms.TextInput(
			attrs={'placeholder':'Age'},
			)
		)