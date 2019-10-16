from django import forms
from recipebox.models import Author
from .models import *


class AuthorsForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)
    exclude = ["user"]


class RecipesForm(forms.ModelForm):

    class Meta:
        model = Recipes
        fields = ['title', 'author', 'description', 'time_req', 'instructions']


    # title = forms.CharField(max_length=50)
    # author = forms.ModelChoiceField(queryset=Author.objects.all())
    # description = forms.CharField(max_length=140)
    # time_req = forms.CharField(max_length=25)
    # instructions = forms.CharField(widget=forms.Textarea)


class SignupForm(forms.Form):
    name = forms.CharField(max_length=500)
    username = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea(attrs={"rows": "3"}))
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
