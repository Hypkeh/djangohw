from django import forms
from django.forms import ModelForm
from .models import Blog, Comment, Messages, Subscibers
from django.contrib.auth.models import User


class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'

class MessagesForm(ModelForm):

    class Meta:
        model = Messages
        fields = '__all__'

class CommentForm(ModelForm):

    class Meta:
        model = Messages
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'
