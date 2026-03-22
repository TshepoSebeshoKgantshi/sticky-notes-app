"""Database models for the notes application."""

from django.db import models


class Note(models.Model):
    """Model representing a single sticky note."""

    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        """Return the note title."""
        return self.title
