from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Game(models.Model):
    MAX_TITLE_LENGTH = 30
    MAX_CATEGORY_LENGTH = 15
    MIN_RATING = 0.1
    MAX_RATING = 5.0
    MAX_LEVEL_MIN_VALUE = 1

    CATEGORIES = (
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Puzzle", "Puzzle"),
        ("Strategy", "Strategy"),
        ("Sports", "Sports"),
        ("Board/Card Game", "Board/Card Game"),
        ("Other", "Other"),
    )

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        unique=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        choices=CATEGORIES,
        null=False,
        blank=False,
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(MIN_RATING),
            MaxValueValidator(MAX_RATING),
        ),
        null=False,
        blank=False,
    )

    max_level = models.IntegerField(
        validators=(
            MinValueValidator(MAX_LEVEL_MIN_VALUE),
        ),
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=False,
        blank=True,
    )
