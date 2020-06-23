from django import forms

class signupform(forms.Form):
	Full_name=forms.CharField(label="",
		max_length=30,
		error_messages={'required':'Please Enter Your Full Name'},
		widget=forms.TextInput(attrs={'Placeholder':'Full Name'}))
	Email=forms.EmailField(label="",
		max_length=30,
		error_messages={'required':'Please Enter Your Email'},
		widget=forms.EmailInput(attrs={'Placeholder':'Email'}))
	PhoneNumber=forms.CharField(label="",
		max_length=30,
		error_messages={'required':'Please Enter Your PhoneNumber'},
		widget=forms.NumberInput(attrs={'Placeholder':'Phone Number'}))
	Password=forms.CharField(label="",
		max_length=30,
		error_messages={'required':'Please Enter Your Password'},
		widget=forms.PasswordInput(attrs={'Placeholder':'Password'}))
	Retype_Password=forms.CharField(label="",
		max_length=30,
		error_messages={'required':'Please Confirm Your Password'},
		widget=forms.PasswordInput(attrs={'Placeholder':'Retype Password'}))
class loginform(forms.Form):
	Email=forms.EmailField(label="",
		max_length=30,
		error_messages={'required':'Please Enter Registered Email'},
		widget=forms.EmailInput(attrs={'Placeholder':'Email'}))
	Password=forms.CharField(label="",
		max_length=30,
		error_messages={'required':'Please Enter Your Password'},
		widget=forms.PasswordInput(attrs={'Placeholder':'Password'}))