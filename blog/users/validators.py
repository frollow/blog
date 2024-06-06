import re

from django.core.exceptions import ValidationError


# Validator for name
def validate_name(value):
    # Ensure the value does not start or end with spaces or hyphens
    if value.startswith((" ", "-")) or value.endswith((" ", "-")):
        raise ValidationError(
            "The name should not start or end with spaces or hyphens."
        )
    # Check for at least one letter
    if not any(char.isalpha() for char in value):
        raise ValidationError("The name must contain at least one letter.")
    # Check for valid characters
    for char in value:
        if not char.isalpha() and not char.isspace() and char != "-":
            raise ValidationError("The name can only contain letters, spaces, and hyphens.")


# Validator for username
def validate_username(value):
    # 1) Ensure the value does not start or end with spaces or hyphens
    if (
        value.startswith("-")
        or value.endswith("-")
        or value.startswith(" ")
        or value.endswith(" ")
    ):
        raise ValidationError(
            "The username should not start or end with spaces or hyphens."
        )

    # 2) The username should not contain spaces
    if " " in value:
        raise ValidationError("The username should not contain spaces.")

    # 3) Check for at least one letter
    if not any(char.isalpha() for char in value):
        raise ValidationError("The username must contain at least one letter.")

    # 4) The username must be at least 5 characters long
    if len(value) < 5:
        raise ValidationError(
            "The username must be at least 5 characters long."
        )

    # 5) The username can only contain lowercase Latin letters, numbers, and hyphens.
    if not re.match(r"^[a-z0-9-]+$", value):
        raise ValidationError(
            "The username can only contain lowercase Latin letters, numbers, and hyphens."
        )

    # 6) Forbidden usernames
    forbidden_usernames = [
        "admin",
    ]
    if value in forbidden_usernames:
        raise ValidationError(f'The username "{value}" is already taken.')
