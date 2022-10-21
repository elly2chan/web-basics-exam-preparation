from django.db import models


class Book(models.Model):
    MAX_TITLE_LENGTH = 30
    MAX_TYPE_LENGTH = 30

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    image = models.URLField(
        null=True,
        blank=True,
    )

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        null=False,
        blank=False,
    )
