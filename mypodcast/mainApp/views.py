from django.shortcuts import render
from userrequest.models import PodcastRequest

def home(request):
    return render(request,"index.html")

def Podcast_Request(request):
    mytitle=mydesc=""
    if request.method == "POST":
        mytitle = request.POST.get("ptopic")
        mydesc = request.POST.get("pdisc")
        print(mytitle,mydesc)
        pd = PodcastRequest(podcast_title = mytitle, podcast_details = mydesc)
        pd.save()
    return render(request,"podcast Request.html")
