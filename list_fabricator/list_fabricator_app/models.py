from django.db import models

# Create your models here.
class UnitDatasheet(models.Model):
    role = models.CharField(max_length=50, null = True, blank = True)
    quantity = models.IntegerField()
    name = models.CharField(max_length=100)
    movement = models.IntegerField()
    weapon_skill = models.IntegerField()
    ballistic_skill = models.IntegerField()
    strength = models.IntegerField()
    toughness = models.IntegerField()
    wounds = models.IntegerField()
    attacks = models.IntegerField()
    leadership = models.IntegerField()
    armor_save = models.IntegerField(null = True, blank = True)
    abilities = models.CharField(max_length=500)
    point_value = models.IntegerField()
    image = models.URLField(null = True, blank = True)
    # wargear = the fixed wargear associated with that unit
    # optional_wargear = the optional wargear associated with that unit

    def __str__(self):
        return self.name

class Wargear(models.Model):
    name = models.CharField(max_length=100)
    range = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)
    armor_penetration = models.IntegerField()
    damage = models.CharField(max_length=200)
    abilities = models.CharField(max_length=500)
    point_value = models.IntegerField()

    def __str__(self):
        return self.name

class OptionalWargear(models.Model):
    weapon = models.CharField(max_length=100)
    imperial_knight_unit = models.ManyToManyField(UnitDatasheet, related_name='optional_wargear')

    def __str__(self):
        return self.weapon

class FixedWargear(models.Model):
    fixed_weapon = models.CharField(max_length=100)
    imperial_knight_unit = models.ManyToManyField(UnitDatasheet, related_name='wargear')

    def __str__(self):
        return self.fixed_weapon