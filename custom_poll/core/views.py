from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.


def test_view(request):
    data = {
        "Name": "Sergey",
        "Age": 34
    }
    return JsonResponse(data)