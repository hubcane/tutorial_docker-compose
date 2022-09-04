from django.contrib import admin
from .models import Tag

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'registered_dtm']

admin.site.register(Tag, TagAdmin)
