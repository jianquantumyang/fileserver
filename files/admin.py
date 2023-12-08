from django.contrib import admin
from .models import UploadedFile

class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_at', 'created_At')
    list_filter = ('created_At',)  # Add 'created_At' to enable filtering

admin.site.register(UploadedFile, UploadedFileAdmin)
