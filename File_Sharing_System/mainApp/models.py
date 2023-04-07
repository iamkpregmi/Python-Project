from django.db import models

class fileSharing(models.Model):
    my_title = models.CharField(max_length=200)
    my_image = models.FileField(upload_to="Uploads/",max_length=250,null=True,default=None)
