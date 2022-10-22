from django.core.validators import MinValueValidator
from django.db import models


class Profile(models.Model):
    MIN_AGE = 12
    MAX_PASSWORD_LENGTH = 30
    MAX_FIRST_NAME_LENGTH = 30
    MAX_LAST_NAME_LENGTH = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(MIN_AGE),
        ),
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        null=False,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        null=False,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
