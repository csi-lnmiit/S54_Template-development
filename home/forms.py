quifrom django import forms

class SignUpForm(forms.Form):
	username = forms.CharField(
		required = True,
		label = 'Username',
		max_length = 32,
		widget=forms.TextInput(
			attrs={'placeholder':'Username'},
			),
	)
	email = forms.CharField(
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
		required = True,
		label = 'Last_Name',
		max_length = 32,
		widget=forms.TextInput(
			attrs={'placeholder':'Last Name'},
			),
		)
	address = forms.CharField(
		required = False,
		label = 'address',
		max_length = 32,
		widget=forms.TextInput(
			attrs={'placeholder':'Address'},
			),
		)