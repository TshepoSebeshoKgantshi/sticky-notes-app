"""Forms for creating and updating sticky notes."""

from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """Form for creating and updating notes."""

    class Meta:
        """Configure the note form fields."""

        model = Note
        fields = ['title', 'content']
