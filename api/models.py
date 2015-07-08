from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=128)
    session = models.CharField(max_length=35,unique=True)

class Box(models.Model):
    bid = models.AutoField(primary_key=True)
    level = models.IntegerField()
    owner = models.ForeignKey("User")

class Party(models.Model):
    uid = models.ForeignKey("User")
    first = models.ForeignKey("Box")
    sec = models.ForeignKey("Box")
    tri = models.ForeignKey("Box")
    qua = models.ForeignKey("Box")

class Monster(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=128)
    initHP = models.IntegerField()
    initAtk = models.IntegerField()
    groHP = models.FloatField()
    groAtk = models.FloatField()
    skill = models.ForeignKey("Skill")

class Skill(models.Model):
    sid = models.AutoField(primary_key=True)
    target = models.CharField(max_length=40)
    function = models.TextField()