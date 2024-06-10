# Rename image name to slug
def rename_img_path_to_slug(path):
    def wrapper(self, filename):
        extension = filename.split(".")[-1]
        return f"{path}/{self.slug}.{extension}"
    return wrapper
