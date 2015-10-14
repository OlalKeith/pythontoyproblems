from django.shortcuts import render
from django.http import HttpResponse
from .forms import Ceaser
# Create your views here.


def index(request):
	form = Ceaser(request.POST or None)
	text = ''
	key = 0
	context = {
		'form':form
	}
	if form.is_valid():
		key = form.cleaned_data.get('key')
		text = form.cleaned_data.get('user_text')
		result = ceaser_cipher(text, key)
		context = {'form':form,'result':result}
	return render(request, 'index.html', context)

def ceaser_cipher(plaintext,key):
	alphabet = "abcdefghijklmnopqrstuvwxyz"

	cipher = ''
	for c in plaintext:
		if c.isalpha():
			cipher += alphabet[alphabet.index(c) +key]
		else:
			cipher+= c
	return cipher