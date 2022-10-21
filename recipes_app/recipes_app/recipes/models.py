from django.db import models

from recipes_app.recipes.validators import ingredients_validator


class Recipe(models.Model):
    MAX_TITLE_LENGTH = 30
    MAX_INGREDIENTS_LENGTH = 250

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=False,
        blank=True,
    )

    ingredients = models.CharField(
        max_length=MAX_INGREDIENTS_LENGTH,
        null=False,
        blank=False,
        validators=(
            ingredients_validator,
        )
    )

    time = models.IntegerField(
        null=False,
        blank=False,
    )
