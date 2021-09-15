from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets,status
from .serializer import *

class QuickPanelView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = QuickPanelSerializer