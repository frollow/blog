from django.utils.deconstruct import deconstructible


# Rename image name to slug
@deconstructible
class RenameImgPathToSlug:
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        extension = filename.split(".")[-1]
        return f"{self.path}/{instance.slug}.{extension}"


# Rename image name to username
@deconstructible
class RenameImgPathToUsername:
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        extension = filename.split(".")[-1]
        return f"{self.path}/{instance.user.username}.{extension}"
