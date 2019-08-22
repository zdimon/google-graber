from django.contrib import admin
from .models import *

class WordAdmin(admin.ModelAdmin):
    pass
admin.site.register(Word, WordAdmin)


class MaterialPageAdmin(admin.ModelAdmin):
    list_display = ['search_url', 'word']
admin.site.register(MaterialPage, MaterialPageAdmin)

class MaterialItemAdmin(admin.ModelAdmin):
    list_display = ['material', 'position', 'link', 'page']
    search_fields = ['link']
admin.site.register(MaterialItem, MaterialItemAdmin)

class LogAdmin(admin.ModelAdmin):
    list_display = ['link', 'created_at']
admin.site.register(Log, LogAdmin)