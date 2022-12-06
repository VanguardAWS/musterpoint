from django.shortcuts import render
from django.http import HttpResponse
from .models import UnitDatasheet, Wargear
from rest_framework import routers, serializers, viewsets
from .serializers import UnitDatasheetSerializer, WargearSerializer
# Create your views here.
def index(request):
    return HttpResponse('ok')

class UnitDatasheetViewSet(viewsets.ModelViewSet):
    queryset = UnitDatasheet.objects.all()
    serializer_class = UnitDatasheetSerializer

class WargearViewSet(viewsets.ModelViewSet):
    queryset = Wargear.objects.all()
    serializer_class = WargearSerializer