from django.db import models

class myToDoList(models.Model):
    toDoListData = models.CharField(max_length=250)
    status = models.BooleanField()
