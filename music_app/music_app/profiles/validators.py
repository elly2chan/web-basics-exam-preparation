from django.core.exceptions import ValidationError


def validate_username_chars(username):
    for char in username:
        if not char.isalnum and not char == '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
