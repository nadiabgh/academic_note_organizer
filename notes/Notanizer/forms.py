from django import forms
from .models import Course, Note
from django.contrib.auth.forms import AuthenticationForm

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']
    
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-blue-400"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
        "class": "w-full px-4 py-3 mt-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-blue-400"})
    )