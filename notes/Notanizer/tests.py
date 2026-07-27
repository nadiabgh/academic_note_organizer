from django.test import TestCase
from django.urls import reverse 
from django.contrib.auth import get_user_model
from .models import Course, Note

User = get_user_model()

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="nadia", password="password123")
    
    def test_create_course(self):
        course = Course.objects.create(title="Advanced Programming", description="Python course", author=self.user)

        self.assertEqual(course.title, "Advanced Programming")
        self.assertEqual(course.description, "Python course")
        self.assertEqual(course.author, self.user)

    def test_create_note(self):
        course = Course.objects.create(title="English", description="IELTS course", author=self.user)
        note = Note.objects.create(title="Vocabulary", description="Band7+ voacbulary", content="First session's notes", course=course)

        self.assertEqual(note.title, "Vocabulary")
        self.assertEqual(note.description, "Band7+ voacbulary")
        self.assertEqual(note.content, "First session's notes")
        self.assertEqual(note.course, course)


class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="nadia", password="password123")
        self.course = Course.objects.create(title="Python", description="Python course", author=self.user)
        self.note = Note.objects.create(title="Functions", description="Functions chapter", content="Inheritance notes", course=self.course)

    def test_home_requires_login(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 302)

    def test_home_logged_in(self):
        self.client.login(username="nadia",password="password123")
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)

    def test_course_detail(self):
        self.client.login(username="nadia",password="password123")
        response = self.client.get(reverse("course_detail", args=[self.course.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python")

    def test_note_detail(self):
        self.client.login(username="nadia", password="password123")

        response = self.client.get(reverse("note_detail", args=[self.note.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Functions")

    def test_cannot_access_other_users_course(self):
        other = User.objects.create_user(username="john", password="password123")
        other_course = Course.objects.create(title="Algorithms", author=other)
        self.client.login(username="nadia", password="password123")
        response = self.client.get(reverse("course_detail", args=[other_course.id]))

        self.assertEqual(response.status_code, 404)

    def test_cannot_access_other_users_note(self):
        other = User.objects.create_user(username="john", password="password123")
        other_course = Course.objects.create(title="Math", author=other)
        other_note = Note.objects.create(title="Limits", course=other_course)
        self.client.login(username="nadia", password="password123")
        response = self.client.get(reverse("note_detail", args=[other_note.id]))

        self.assertEqual(response.status_code, 404)

    def test_search_course(self):
        self.client.login(username="nadia", password="password123")
        response = self.client.get(reverse("search"), {"q": "Python"})

        self.assertContains(response, "Python")

    def test_search_note(self):
        self.client.login(username="nadia", password="password123")
        response = self.client.get(reverse("search"), {"q": "Functions"})

        self.assertContains(response, "Functions")

    def test_search_no_results(self):
        self.client.login(username="nadia", password="password123")
        response = self.client.get(reverse("search"), {"q": "Java"})

        self.assertEqual(len(response.context["course_results"]), 0)
        self.assertEqual(len(response.context["note_results"]), 0)

    def test_course_str(self):
        course = Course.objects.create(title="Algorithms", author=self.user)

        self.assertEqual(str(course), "Algorithms")

    def test_note_str(self):
        course = Course.objects.create(title="Python", author=self.user)
        note = Note.objects.create(title="Loops", course=course)

        self.assertEqual(str(note), "Loops")
    
    def test_create_course(self):
        self.client.login(username="nadia", password="password123")

        response = self.client.post(reverse("create_course"), {"title": "Networks", "description": "Computer Networks"})

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Course.objects.filter(title="Networks").exists())
    
    def test_create_note(self):
        self.client.login(username="nadia",password="password123")
        response = self.client.post(reverse("create_note", args=[self.course.id]), {"title": "Loops", "description": "Loop chapter", "content": "for loop"})

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title="Loops").exists())

    def test_delete_course(self):
        self.client.login(username="nadia", password="password123")
        self.client.post(reverse("delete_course", args=[self.course.id]))

        self.assertFalse(Course.objects.filter(id=self.course.id).exists())
    
    def test_delete_note(self):
        self.client.login(username="nadia", password="password123")
        self.client.post(reverse("delete_note", args=[self.note.id]))

        self.assertFalse(Note.objects.filter(id=self.note.id).exists())
    
    def test_edit_course(self):
        self.client.login(username="nadia", password="password123")
        self.client.post(reverse("edit_course", args=[self.course.id]), {"title": "Advanced Python", "description": "Updated"})
        self.course.refresh_from_db()
        self.assertEqual(self.course.title, "Advanced Python")

    def test_edit_note(self):
        self.client.login(username="nadia", password="password123")
        self.client.post(reverse("edit_note", args=[self.note.id]), {"title": "Updated Functions", "description": "Updated", "content": "Updated notes"})
        self.note.refresh_from_db()

        self.assertEqual(self.note.title, "Updated Functions")