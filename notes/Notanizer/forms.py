from django import forms
from .models import Course, Note
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']
        widgets = {
            "title": forms.TextInput(attrs={"class": "w-full px-4 py-3 mt-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-blue-400"}),
            "description": forms.Textarea(attrs={"class": "w-full px-4 py-3 mt-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-blue-400 resize-none","rows": 4}),
        }
    
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description', 'content']
        widgets = {
            "title": forms.TextInput(attrs={"class": "w-full px-4 py-3 mt-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-blue-400"}),
            "description": forms.Textarea(attrs={"class": "w-full px-4 py-3 mt-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-blue-400 resize-none","rows": 4}),
            "content": forms.Textarea(attrs={"class": "w-full px-4 py-3 mt-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-blue-400 resize-none","rows": 4}),
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-blue-400"})
        )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
        "class": "w-full px-4 py-3 mt-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-blue-400"})
        )

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-blue-400"})
        )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
        "class": "w-full px-4 py-3 mt-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-blue-400"})
        )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
        "class": "w-full px-4 py-3 mt-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-blue-400"})
        )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "w-full px-4 py-3 mt-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-blue-400"})
        )

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]
