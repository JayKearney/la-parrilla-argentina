from django.db import models

# Create your models here.


class Meats(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to='menu/')

    
    def __str__(self):
        return self.name
