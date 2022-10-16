from re import L
from django.shortcuts import render

def index(request):
    name = "Richard"
    return render(request, "index.html", locals())
