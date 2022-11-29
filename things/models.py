from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# model named thing with 3 attributes; name, description, and quantity
class Thing(models.Model):
    name = models.CharField(
        max_length=30, 
        unique=True, 
        blank=False
        )
    description = models.TextField(
        unique=False, 
        blank=True, 
        max_length=120
        )
    quantity = models.IntegerField(
        unique=False, 
        blank=False, 
        default=0, 
        validators=[
            MinValueValidator(0), 
            MaxValueValidator(100)
            ]
        )
        

    # returns the name of the thing
    def __str__(self):
        return self.name