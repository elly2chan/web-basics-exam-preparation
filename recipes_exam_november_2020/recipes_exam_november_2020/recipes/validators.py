from django.forms import models


def ingredients_validator(value):
    if ',' not in value:
        raise models.ValidationError('The ingredients must be separated by ","')
