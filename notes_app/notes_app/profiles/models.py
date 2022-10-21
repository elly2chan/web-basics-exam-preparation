from django.db import models


class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 20
    MAX_LAST_NAME_LENGTH = 20

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

