from django.shortcuts import render_to_response
from nltk.corpus import brown
from random import choice

# Create your views here.
word_list = brown.words()

def find_word():
	x = choice(word_list)
	while len(x) <= 2 or not x.isalpha():
		x = choice(word_list)
	return x

def home(request):
	word1 = find_word()
	word2 = find_word()
	word3 = find_word()
	return render_to_response("Generate_Words/home.html", {"word_list" : [word1, word2, word3]})
