from re import L
from django.shortcuts import render
import random

def index(request):
    name = "Richard"
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    lotto = sorted(numbers[:6])
    return render(request, "index.html", locals())
