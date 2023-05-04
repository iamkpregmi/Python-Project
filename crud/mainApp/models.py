from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    salary = models.IntegerField()
    city = models.CharField(max_length=30, default="",null=True,blank=True)

    def __str__(self):
        return str(self.id)+' '+self.name
