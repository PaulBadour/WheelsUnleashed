from django.shortcuts import render, HttpResponse
from .models import TestModel
# Create your views here.
def home(request):
    return render(request, "base.html")

def adminDB(request):
    items = TestModel.objects.all()
    return render(request, "testDB.html", {"items": items})