from ExamPrep_II.fruits.validators import OnlyLettersValidator
from django.core.validators import MinLengthValidator
from django.db import models


class Fruit(models.Model):
    name = models.CharField(
        unique=True,
        max_length=30,
        validators=[
            MinLengthValidator(2),
            OnlyLettersValidator(),
        ],
        error_messages={
            'unique': "This fruit name is already in use! Try a new one."
        }
    )

    image_url = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(
        blank=True,
        null=True,
    )

    owner = models.ForeignKey(
        to="profiles.Profile",
        on_delete=models.CASCADE,
        related_name='fruits',
    )

