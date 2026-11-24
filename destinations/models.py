from django.db import models

class Transportation(models.Model):
    name = models.CharField(max_length=100)


class Interest(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

class Place(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    rating = models.FloatField(default=0)
    image = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    interests = models.ManyToManyField(
        Interest,
        related_name="places"
    )

    