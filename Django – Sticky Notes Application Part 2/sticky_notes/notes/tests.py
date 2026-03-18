from django.test import TestCase
from django.urls import reverse

from .models import Note


class NoteModelTest(TestCase):
    def test_note_string_representation_returns_title(self):
        note = Note.objects.create(title="Shopping List", content="Buy milk")
        self.assertEqual(str(note), "Shopping List")


class NoteViewTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Study Django",
            content="Review views, forms, and templates",
        )

    def test_note_list_view_displays_saved_note(self):
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Study Django")
        self.assertContains(response, "Review views, forms, and templates")

    def test_note_detail_view_displays_note(self):
        response = self.client.get(reverse("note_detail", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Study Django")
        self.assertContains(response, "Review views, forms, and templates")

    def test_create_note_adds_a_new_note(self):
        response = self.client.post(
            reverse("note_create"),
            {"title": "Plan project", "content": "Write unit tests"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title="Plan project").exists())

    def test_update_note_changes_saved_content(self):
        response = self.client.post(
            reverse("note_update", args=[self.note.pk]),
            {
                "title": "Study Django Well",
                "content": "Run the sticky notes test suite",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Study Django Well")
        self.assertEqual(self.note.content, "Run the sticky notes test suite")

    def test_delete_note_removes_it_from_the_database(self):
        response = self.client.get(reverse("note_delete", args=[self.note.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
