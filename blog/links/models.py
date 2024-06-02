from django.db import models


class ProcessedLink(models.Model):
    link = models.URLField(unique=True, db_index=True)
    processed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link
