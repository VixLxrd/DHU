from django.shortcuts import render

def home_render(request):
    return(render(request, 'home.html'))
