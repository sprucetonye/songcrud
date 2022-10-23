from platform import release
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    
    def __str__(self):
        return self.first_name # + '' + self.first_name

class Song(models.Model):
    title = models.CharField(max_length=250)
    release = models.CharField(max_length=200)
    likes = models.CharField(max_length=200)
    artiste_id = models.ForeignKey(Artiste, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title # + '' + self.title
    

    
    
class Lyric(models.Model):
    # content, song_id
    content = models.CharField(max_length=200)
    song_id = models.ForeignKey(Song, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content # + '' + self.content