from django.contrib import admin
from .models import Note#, Tag

# Register your models here.
# class TagInline(admin.StackedInline):
#     model = Tag
#     filter_horizontal = ('tags',)




class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'pub_date', 'was_published_recently')
    # list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


admin.site.register(Note, NoteAdmin)

