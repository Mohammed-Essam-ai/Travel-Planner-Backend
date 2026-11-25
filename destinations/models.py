from django.db import models

class Transportation(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name


class Interest(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    def __str(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    rating = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    city=models.CharField(max_length=255)
    interests = models.ManyToManyField(
        Interest,
        related_name="places"
    )

class Budget(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str(self):
        return self.name

class TripType(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str(self):
        return self.name     