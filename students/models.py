from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(80)]
    )
    email = models.EmailField(unique=True)
