from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('book',BookViewSet.as_view,name="bookviewset"),
]
