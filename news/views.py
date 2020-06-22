from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .models import *
from .serializers import *
from django.views import View
# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self,request,*args,**kwargs):
        title = request.data['title']
        cover = request.data['cover']
        Book.objects.create(title=title,cover=cover)
        return HttpResponse({'message':'Book Create'},status=200)