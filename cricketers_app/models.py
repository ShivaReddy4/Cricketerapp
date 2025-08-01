# cricketers_app/models.py

from django.db import models

class Cricketer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    role = models.CharField(max_length=50)  # e.g., Batsman, Bowler
    batting_style = models.CharField(max_length=100, blank=True)
    bowling_style = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name
