from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm


@login_required
def home(request):
    courses = Course.objects.order_by('-created')
    return render(request, 'home.html', {'courses': courses})

class CustomLoginView(LoginView):
    template_name="registration/login.html"
    authentication_form = CustomAuthenticationForm


