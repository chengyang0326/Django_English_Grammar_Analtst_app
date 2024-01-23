from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Sentences
from .forms import CreateNewInput
from django.http import HttpResponseRedirect
from .forms import UserRegistration

from  .Englishgrammar import *
from .models import POS
from .models import Document
from .forms import UploadFileForm




def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'registration/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'registration/signup.html', context=context)


def index(response,id):

	pos= POS.objects.get(id=id)
	return render(response,"dashboard.html",{"pos":pos})
def create(response):
	if response.method=="POST":
		form=CreateNewInput(response.POST)
		if form.is_valid():
			print("form: ",form)
			n=form.cleaned_data["text"]
			
			print("n: ",n)
			
			
			parse_to_backend(n)
			
			t=POS(sentence=sentence_counter,noun=noun_counter,verb=verb_counter,article=article_counter,proposition=proposition_counter,pronoun=pronoun_counter,space=space_counter,adjective=adverb_counter,adverb=adverb_counter,Question_word=Question_word_counter,punctation=punctation_counter)
			t.save()
		return redirect("/%i" %t.id)

	else:


		form=CreateNewInput()
	return render(response,"create.html",{"form":form})

def parse_to_backend(string):
	global sentence_counter
	global noun_counter
	global verb_counter
	global article_counter
	global proposition_counter
	global pronoun_counter
	global space_counter
	global adjective_counter
	global adverb_counter
	global Question_word_counter
	global punctation_counter

	parse_tree=grammar.parse(string)

	parse_tree_string=str(parse_tree)
	print(parse_tree_string)
	sentence_counter=parse_tree_string.count("sentence")
	noun_counter = parse_tree_string.count("noun")
	verb_counter= parse_tree_string.count("verb")
	article_counter=parse_tree_string.count("article")
	proposition_counter= parse_tree_string.count("proposition")
	pronoun_counter=parse_tree_string.count("pron")
	space_counter=parse_tree_string.count("space")
	adjective_counter=parse_tree_string.count("adjective")
	adverb_counter=parse_tree_string.count("adv")
	Question_word_counter=parse_tree_string.count("Question_word")
	punctation_counter= parse_tree_string.count("punctation")

	
	return(sentence_counter,noun_counter,verb_counter,article_counter,proposition_counter,pronoun_counter,space_counter,adjective_counter,adverb_counter,Question_word_counter,punctation_counter)


def model_form_upload(request):
	if request.method=='POST':
		form=UploadFileForm(request.POST,request.FILES)
		if form.is_valid():
			f = request.FILES['file']
			file_contents = f.read()
			file_contents_str = file_contents.decode()
			print(file_contents_str)
			print(type(file_contents_str)) 
			data = file_contents_str.split("\cf0 ") 
			data = data[1].strip('}')
			print(data)

			
			parse_to_backend(data)
			t=POS(sentence=sentence_counter,noun=noun_counter,verb=verb_counter,article=article_counter,proposition=proposition_counter,pronoun=pronoun_counter,space=space_counter,adjective=adverb_counter,adverb=adverb_counter,Question_word=Question_word_counter,punctation=punctation_counter)
			t.save()
			
			
			

			return redirect("/%i" %t.id)

	else:
		form=UploadFileForm()
	return render(request,'model_form_upload.html',{'form':form})

