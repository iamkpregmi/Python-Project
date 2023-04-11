from django.shortcuts import render
from django.http import HttpResponse

def home(response):
    return HttpResponse("Welcome to the Home Page")

def blog(response,blog_id):
    return HttpResponse(blog_id)

