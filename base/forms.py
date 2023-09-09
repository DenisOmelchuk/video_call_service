from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, GameRoom


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Create a password'}))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'inputfile', 'id': 'file'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Create a username'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'avatar']




class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))


class RoomCreationForm(forms.ModelForm):
    room_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Create a room name'}))
    username = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter number of players'}))

    class Meta:
        model = GameRoom
        fields = ['room_name', 'necessary_number_of_players']


