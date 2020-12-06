from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Command
from .serializer import CommandSerializer

# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")

class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
