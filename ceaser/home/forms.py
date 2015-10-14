from django import forms

class Ceaser(forms.Form):
	user_text = forms.CharField(label="Enter text",min_length =1, max_length =10)
	key = forms.CharField(label="Enter key",min_length =1, max_length =10)