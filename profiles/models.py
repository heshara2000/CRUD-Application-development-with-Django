from django.db import models

# Create your models here.
from django.core.validators import RegexValidator, MinValueValidator


class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
    max_length=20,
    blank=True,
    validators=[RegexValidator(r'^\d{10}$', "Phone must contain exactly 10 digits")]
    )
    address = models.TextField(blank=True)
    age = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} <{self.email}>"