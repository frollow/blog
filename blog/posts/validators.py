import re

from django.core.exceptions import ValidationError


# Validator for post name
def validate_post_name(value):
    # Ensure the value does not start or end with spaces or hyphens
    if value.startswith((" ", "-")) or value.endswith((" ", "-")):
        raise ValidationError(
            "The name should not start or end with spaces or hyphens."
        )
    # Check for the presence of at least one letter
    if not any(char.isalpha() for char in value):
        raise ValidationError("The post name must contain at least one letter.")


# Validator for image
# Check file size
def validate_image_size(image):
    errors = []
    # Check image size
    file_size = image.file.size
    limit = 1 * 1024 * 1024  # 1 megabyte
    if file_size > limit:
        errors.append("The file size must not exceed 1 megabyte.")
    if errors:
        raise ValidationError(" ".join(errors))


def validate_file_extension(value):
    ext = value.name.split(".")[-1]  # get file extension
    valid_extensions = ["jpg", "jpeg", "png"]
    if ext.lower() not in valid_extensions:
        raise ValidationError(
            "File format is not supported. Only JPG, JPEG, or PNG files are allowed."
        )


# Validator for text field
URL_REGEX = (
    r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
)
HTML_LINK_REGEX = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"'


def validate_links_in_input(value):
    # Check for the presence of HTML links
    if re.search(HTML_LINK_REGEX, value):
        raise ValidationError("HTML links are not allowed in the text.")
    # Check for the presence of simple links
    if re.search(URL_REGEX, value):
        raise ValidationError("Links are not allowed in the text.")


# Validator for slug
def validate_slug(value):
    # 1) Ensure the value does not start or end with spaces or hyphens
    if (
        value.startswith("-")
        or value.endswith("-")
        or value.startswith(" ")
        or value.endswith(" ")
    ):
        raise ValidationError(
            "The slug should not start or end with spaces or hyphens."
        )

    # 2) The slug should not contain spaces
    if " " in value:
        raise ValidationError("The slug should not contain spaces.")

    # 3) Check for the presence of at least one letter
    if not any(char.isalpha() for char in value):
        raise ValidationError("The slug must contain at least one letter.")

    # 4) The slug length should be at least 5 characters
    if len(value) < 5:
        raise ValidationError("The slug must be at least 5 characters long.")

    # 5) The slug can only contain lowercase Latin letters, numbers, and hyphens.
    if not re.match(r"^[a-z0-9-]+$", value):
        raise ValidationError(
            "The slug can only contain lowercase Latin letters, numbers, and hyphens."
        )

    # 6) Forbidden usernames
    forbidden_usernames = [
        "admin",
    ]
    if value in forbidden_usernames:
        raise ValidationError(f'The name "{value}" is already taken.')
