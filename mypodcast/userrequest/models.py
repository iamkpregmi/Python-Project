from django.db import models

class PodcastRequest(models.Model):
    podcast_title = models.CharField(max_length=100)
    podcast_details = models.TextField()
