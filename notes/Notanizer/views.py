from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Note
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm, CourseForm, NoteForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

@login_required
def home(request):
    courses = Course.objects.order_by('-created')
    return render(request, 'courses/list.html', {'courses': courses})

class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = CustomAuthenticationForm

class CustomSignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    
@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id, author=request.user)
    return render(request, 'courses/detail.html', {'course': course})

@login_required
def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id, author=request.user)
    return render(request, 'notes/detail.html', {'note': note})

@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.author = request.user
            course.save()
            return redirect('home')
    else:
        form = CourseForm()
    return render(request, 'courses/form.html', {'form': form})

@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, author=request.user)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/form.html', {'form': form})

@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, author=request.user)
    if request.method == 'POST':
        course.delete()
        return redirect('home')
    return render(request, 'courses/delete.html', {'course': course})

@login_required
def create_note(request, course_id):
    course = get_object_or_404(Note, id=course_id, author = request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.course = course
            note.save()
            return redirect('course_detail', course_id=course.id)
        else:
            form = NoteForm()
        return render(request, 'notes/form.html', {'form': form, 'course': course})

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, course__author = request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', note_id=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/form.html', {'form': form})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, course__author = request.user)
    if request.method == 'POST':
        course_id = note.course.id
        note.delete()
        return redirect('course_detail', course__author=request.user)
    return render(request, 'notes/delete.html', {'note': note})
