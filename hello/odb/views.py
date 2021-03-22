from django.shortcuts import render
from .models import Home


def index(request):
    homes = Home.objects.all()

    return render(request, 'index.html', {'homes': homes})
