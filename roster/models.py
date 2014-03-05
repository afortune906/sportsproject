from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(unique=True, max_length=50)
    height = models.CharField(unique=False, max_length=5)
    year = models.CharField(unique=False, max_length=10)
    hometown = models.CharField(unique=False, max_length=30)
    highschool = models.CharField(unique=False, max_length=50)
    imageurl = models.TextField()
    major = models.CharField(unique=False, max_length=40)
    experience = models.CharField(unique=False, max_length =15)
    fallstatssingles = models.CharField(unique=False, max_length=10)
    fallstatsdoubles = models.CharField(unique=False, max_length=10)
    careerstatssingles = models.CharField(unique=False, max_length=10)
    careerstatsdoubles = models.CharField(unique=False, max_length=10)
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
    
