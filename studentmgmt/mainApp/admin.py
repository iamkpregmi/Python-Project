from django.contrib import admin
from .models import student

class studentAdmin(admin.ModelAdmin):
    list_display = ("roll_no","name","fee")
    search_fields = ["name"]
admin.site.register(student,studentAdmin)