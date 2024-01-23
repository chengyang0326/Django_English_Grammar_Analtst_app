

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django import forms
# from .models import Profile
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import UserRegistrationModel
from django.contrib.auth.forms import PasswordResetForm
from .models import Document
from .models import POS
from .models import Sentences


class CreateNewInput(forms.ModelForm):
    class Meta:
        model = Sentences
        fields = ('text', )
	

class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']


class UploadFileForm(forms.Form):
    file = forms.FileField()


class POSForm(forms.ModelForm):
	class Meta:
		model=POS
		fields=('sentence','noun','verb','article','proposition','pronoun','adjective','adverb','space','Question_word','punctation')


