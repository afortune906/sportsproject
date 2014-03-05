from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(unique=True, max_length=80)
    height = models.CharField(unique=False, max_length=50)
    year = models.CharField(unique=False, max_length=100)
    hometown = models.CharField(unique=False, max_length=100)
    highschool = models.CharField(unique=False, max_length=100)
    imageurl = models.TextField()
    major = models.CharField(unique=False, max_length=100)
    experience = models.CharField(unique=False, max_length =150)
    fallstatssingles = models.CharField(unique=False, max_length=100)
    fallstatsdoubles = models.CharField(unique=False, max_length=100)
    careerstatssingles = models.CharField(unique=False, max_length=100)
    careerstatsdoubles = models.CharField(unique=False, max_length=100)
    maplink = models.TextField()
    music = models.TextField()
    food = models.TextField()
    job = models.TextField()
    celebrity = models.TextField()
    description = models.TextField()
   
    def __unicode__(self):
        return U'%s' %(self.name)
 
    
    
class Team(models.Model):
    name = models.CharField(unique=True, max_length=80)
    headcoach = models.CharField(unique=False, max_length=30)
    description = models.TextField()
    icon = models.TextField()
    teamimageurl = models.TextField()
    players = models.ManyToManyField(Player)
    def __unicode__(self):
        return U'%s' %(self.name)
    
