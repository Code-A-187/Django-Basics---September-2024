from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from ExamPrep.albums.choices import GenreChoices
from ExamPrep.profiles.validators import AlphanumericValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            AlphanumericValidator(),
        ]
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
