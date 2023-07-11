from django.shortcuts import render
from django.http import HttpResponse
from .models import Tag_Value, Tag

# Create your views here.
def index(request):
    version = Tag_Value.get_value("app.version@")
    return HttpResponse(f"Hola, estás en el svn_monitor, version {version}")