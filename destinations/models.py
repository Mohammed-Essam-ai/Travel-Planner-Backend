from django.db import models
from django.contrib.auth.models import User

class Transportation(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name


class Interest(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    address = models.TextField()
    region=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    continent=models.CharField(max_length=255)
    interests = models.ManyToManyField(
        Interest,
        related_name="places"
    )
    rating = models.FloatField(default=0)


class FavouritePlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favourite_places")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="favourited_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "favourite_places"
        constraints = [
            models.UniqueConstraint(fields=["user", "place"], name="unique_user_favourite_place")
        ]

    def __str__(self):
        return f"{self.user} - {self.place}"

class Budget(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str(self):
        return self.name

class TripType(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str(self):
        return self.name  
        