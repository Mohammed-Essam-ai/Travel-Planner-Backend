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
    is_active = models.BooleanField(default=True)
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

class Budget(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str(self):
        return self.name

class TripType(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str(self):
        return self.name     



#                                         attraction
# attraction_id attraction_name attraction_country(string) attraction_address(string) attraction_region(string)  attraction_city(string)  attraction_continent(string)   attracion_type(foreign_key)  attraction_rating(float)  

#                                         Mode عندى فى الباك التايب  
# mode_id  mode_name 

#                                       type/interest
# type_id   type_name                                        


                                        
