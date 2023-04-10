from django.db import models

class student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=50)
    fee = models.DecimalField(max_digits=9,decimal_places=2)