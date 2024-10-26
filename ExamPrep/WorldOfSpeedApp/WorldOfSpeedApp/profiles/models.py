from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator

from WorldOfSpeedApp.cars.validators import UsernameValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3),
            UsernameValidator(),
        ],
        error_messages={
            'MinLengthValidator': "Username must be at least 3 chars long!"
        }
    )

    email = models.EmailField()

    age = models.IntegerField(
        validators=[
            MinValueValidator(21)
        ],
        help_text="Age requirement: 21 years and above."
    )

    password = models.CharField(
        max_length=20,
    )

    first_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

