from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from music_app.profiles.validators import validate_username_chars


class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH),
            validate_username_chars,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(0),
        ),
        null=True,
        blank=True,
    )
