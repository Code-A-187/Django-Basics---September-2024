from django.core.validators import MinLengthValidator
from django.db import models

from ExamPrep_II.profiles.validators import FirstCharValidator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(2),
            FirstCharValidator(),
        ]
    )

    last_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(1),
            FirstCharValidator(),
        ]
    )

    email = models.EmailField(
        unique=True,
        max_length=40,
    )

    password = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(8),
        ],
        help_text="*Password length requirements: 8 to 20 characters"
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    age = models.IntegerField(
        default=18,
        blank=True,
        null=True,
    )