from django.db import models
from django.core.validators import RegexValidator

class Room(models.Model):
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, max_length=5)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='room_images/')
    
    landlord_name = models.CharField(max_length=100)
    
    # Validator to allow only numbers and ensure it's of length 10 (for example)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    landlord_phone = models.CharField(max_length=15, validators=[phone_regex])

    def __str__(self):
        return self.location
