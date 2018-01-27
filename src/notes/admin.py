from django.contrib import admin
from .models import Note, Book, Tag


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'get_viewers', 'get_editors', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'owner', 'get_editors', 'get_viewers', 'notes')

class TagAdmin(admin.ModelAdmin):
    list_display = ('body', 'owner')


admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Book, BookAdmin)