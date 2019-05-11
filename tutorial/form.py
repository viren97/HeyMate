from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    email = forms.EmailField(required =True)

    class Meta:
        model = User
        fields =('username','email','firstname', 'lastname','password1','password2')

    def save(self, commit=True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']

        if commit:
            user.save()
        return user
