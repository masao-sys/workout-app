from django.urls import path
from api import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]