from django.db import models


class Note(models.Model):
    MAX_TITLE_LENGTH = 30

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    content = models.TextField(
        null=False,
        blank=False,
    )
