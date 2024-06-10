import os.path

from sorl.thumbnail.base import EXTENSIONS, ThumbnailBackend
from sorl.thumbnail.conf import settings
from sorl.thumbnail.helpers import serialize, tokey


# Rename thumbnail image name to slug
class KeepNameThumbnailBackend(ThumbnailBackend):
    def _get_thumbnail_filename(self, source, geometry_string, options):
        """
        Computes the destination filename.
        """
        key = tokey(source.key, geometry_string, serialize(options))
        # make some subdirs
        path = "%s/%s/%s" % (key[:2], key[2:4], key)
        filename, _ext = os.path.splitext(os.path.basename(source.name))
        return "%s%s/%s.%s" % (
            settings.THUMBNAIL_PREFIX,
            path,
            filename,
            EXTENSIONS[options["format"]],
        )
