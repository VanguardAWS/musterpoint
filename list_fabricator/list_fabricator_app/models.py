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

    def __str__(self):
        return self.name

class Wargear(models.Model):
    name = models.CharField(max_length=100)
    range = models.IntegerField()
    type = models.CharField(max_length=100)
    strength = models.IntegerField()
    armor_penetration = models.IntegerField()
    damage = models.IntegerField()
    abilities = models.CharField(max_length=500)
    point_value = models.IntegerField()

    def __str__(self):
        return self.name