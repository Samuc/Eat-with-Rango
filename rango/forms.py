from django import forms
from rango.models import Tapa, Bar, UserProfile
from django.db import models
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)



class BarForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Please enter the bar name.")
    direccion = forms.CharField(max_length=128, help_text="Please enter the address of the bar.", required=True)
    visitas = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Bar
        fields = ('nombre', 'direccion')


class TapaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Please enter the name of the tapa and select the bar.")
    votos = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tapa

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the bar field from the form,
        exclude = ('url',)
        #or specify the fields to include (i.e. not include the bar field)
        #fields = ('title', 'url', 'views')
        fields = ('nombre', 'bar', 'votos')
