from rest_framework import serializers
from .models import UnitDatasheet, Wargear, OptionalWargear, FixedWargear

class OptionalWargearSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('weapon')
        model = OptionalWargear

class FixedWargearSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('fixed_weapon')
        model = FixedWargear

class WargearSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Wargear


class UnitDatasheetSerializer(serializers.ModelSerializer):
    wargear = serializers.StringRelatedField(many=True, read_only=True)
    optional_wargear = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        fields = ('role', 'quantity', 'name', 'movement', 'weapon_skill', 'ballistic_skill', 'strength', 'toughness', 'wounds', 'attacks', 'leadership', 'armor_save', 'abilities', 'point_value', 'image', 'wargear', 'optional_wargear')
        model = UnitDatasheet