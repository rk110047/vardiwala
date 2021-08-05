from django.db import models

# Create your models here.
class City(models.Model):
    name            =       models.CharField(max_length=500)


    def __str__(self):
        return self.name



class State(models.Model):
    name            =       models.CharField(max_length=500)


    def __str__(self):
        return self.name