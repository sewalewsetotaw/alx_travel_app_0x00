# listings/urls.py
from django.urls import path
from .views import SampleAPIView

urlpatterns = [
    path('sample/', SampleAPIView.as_view()),
]
