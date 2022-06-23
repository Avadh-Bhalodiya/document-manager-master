from django.contrib import admin

from .models import DocumentTemplate, GeneratedDocument

# Register your models here.

admin.site.register(DocumentTemplate)
admin.site.register(GeneratedDocument)