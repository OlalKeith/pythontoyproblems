from django.shortcuts import render
from django.http import HttpResponse
from .forms import Ceaser
# Create your views here.


def index(request):
	form = Ceaser(request.POST or None)
	context = {
		'form':form
	}
	
	result = ceaser_cipher(input)
	return render(request, 'index.html' , context)

def ceaser_cipher(plaintext):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	num = 2

	cipher = ''
	for c in plaintext:
		if c.isalpha():
			cipher += alphabet[(alphabet.index(c)+ num)]
		else:
			cipher+= c
	return cipher