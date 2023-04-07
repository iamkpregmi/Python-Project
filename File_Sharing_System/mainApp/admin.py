from django.contrib import admin
from .models import fileSharing

class fileSharingAdmin(admin.ModelAdmin):
    list_display = ["my_title","my_image"]

admin.site.register(fileSharing,fileSharingAdmin)
