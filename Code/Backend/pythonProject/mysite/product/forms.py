from django import forms
from django.contrib.auth.models import User

from .models import Profile

from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )
        widgets = {
            'username': forms.TextInput(attrs = {'class': "form-control"}),
            'email': forms.EmailInput(attrs = {"class": "form-control"}),
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),

        }

        def clean_username(self):
            username = self.cleaned_data['username'].lower()
            r = User.objects.filter(username=username)
            if r.count():
                raise forms.ValidationError("Username already exists")
            return username

        def clean_email(self):
            email = self.cleaned_data['email'].lower()
            r = User.objects.filter(email=email)
            # if r.count():
            #   raise forms.ValidationError("Email already exists")
            return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'avatar',
        )

        widgets = {
            'avatar' : forms.FileInput(attrs = {'onchange': 'loadFile (event)',})
        }

class SearchForm(forms.Form):
    search = forms.CharField(max_length= 30, widget=forms.TextInput(attrs = {'class' : "form-control", 'id': "search", 'placeholder' : "Search Place"}))

class ReviewForm(forms.Form):
    comment = forms.CharField(max_length= 100, widget = forms.Textarea(attrs={'class':"form-control",'placeholder':"write a comment...",'rows':"3"}))
    rating = forms.IntegerField(max_value=5)