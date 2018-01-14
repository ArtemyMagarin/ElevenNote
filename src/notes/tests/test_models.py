from django.utils import timezone
from django.test import TestCase

from notes.models import Note

class NoteMethodTests(TestCase):

    def test_was_published_recently(self):
        """
        was_published_recently() should return False for notes whose pub_date is in the future.
        """
        time = timezone.now() + timezone.timedelta(days=30)
        future_note = Note(pub_date=time)
        self.assertEqual(future_note.was_published_recently(), False)