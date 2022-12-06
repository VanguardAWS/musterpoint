from rest_framework import serializers
from .models import UnitDatasheet, Wargear

class UnitDatasheetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = UnitDatasheet

class WargearSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Wargear