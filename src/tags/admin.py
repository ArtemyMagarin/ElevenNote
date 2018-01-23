from django.contrib import admin
from .models import Tag
# Register your models here.

class TagAdmin(admin.ModelAdmin):
	list_display = ('body', 'owner')
	list_filter = ['owner']


admin.site.register(Tag, TagAdmin)