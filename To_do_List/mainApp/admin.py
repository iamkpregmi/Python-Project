from django.contrib import admin
from .models import myToDoList

class myToDoListAdmin(admin.ModelAdmin):
    list_display = ["toDoListData", "status"]

admin.site.register(myToDoList,myToDoListAdmin)
