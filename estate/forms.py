from django.forms import ModelForm
from django import forms
from .models import House, Profile, Agents
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = ('name', 'address', 'description', 'price', 'image')


class SignupForm(UserCreationForm):
    full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User 
        fields = ['full_name', 'username', 'email', 'password1', 'password2']
        
        
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['class']= 'form-control'

class ProfileForm(ModelForm):
    
    class Meta:
        model = Agents
        fields = ("name","phone_number", "email")
