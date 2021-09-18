from django.db import models
from .utils import create_shortened_url


class ShortLink(models.Model):

    time_of_creation = models.DateTimeField(auto_now_add=True)
    count_url = models.PositiveIntegerField(default=0)
    longer_url = models.URLField(unique=True)
    shorter_url = models.CharField(max_length=6, unique=True, blank=True)

    class Meta:
        ordering = ["-time_of_creation"]

    def __str__(self):
        return f'{self.longer_url} to {self.shorter_url}'

    def save(self, *args, **kwargs):
        if not self.shorter_url:
            self.shorter_url = create_shortened_url(self)

        super().save(*args, **kwargs)
