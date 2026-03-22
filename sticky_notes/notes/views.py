"""Views for the sticky notes CRUD workflow."""

from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note


def note_list(request):
    """Display all sticky notes."""
    notes = Note.objects.all()
    context = {
        'notes': notes,
        'page_title': 'My Sticky Notes',
    }
    return render(request, 'notes/note_list.html', context)


def note_detail(request, pk):
    """Display one sticky note."""
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})


def note_create(request):
    """Create a new sticky note."""
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()

    return render(request, 'notes/note_form.html', {'form': form})


def note_update(request, pk):
    """Update an existing sticky note."""
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/note_form.html', {'form': form})


def note_delete(request, pk):
    """Delete a sticky note and return to the list view."""
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')
