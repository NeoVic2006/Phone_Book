from django.urls import path, include
from .views import Poll, Questions

app_name ="Poll"

urlpatterns = [
    path('', Poll.as_view(), name="Poll"),
    path('<str:topic>/', Questions.as_view(), name="question"),
]
