from django import forms

class Ceaser(forms.Form):
	user_text = forms.CharField(label="Enter text",min_length =1, max_length =100)
	key = forms.IntegerField(label="Enter key")