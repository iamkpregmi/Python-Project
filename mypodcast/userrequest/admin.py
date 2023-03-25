from django.contrib import admin
from userrequest.models import PodcastRequest

class podcastAdmin(admin.ModelAdmin):
    list_display = ("podcast_title","podcast_details")

admin.site.register(PodcastRequest,podcastAdmin)
