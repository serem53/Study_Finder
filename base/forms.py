from django.forms import ModelForm
from .models import Room,User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','password1','password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        exclude = ['host', 'participants']  # Replace with the field names you want to exclude


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username', 'email', 'bio']