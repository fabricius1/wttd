from django.db import models
from django.shortcuts import resolve_url as r


class Speaker(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    photo = models.URLField()
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'speaker'
        verbose_name_plural = 'speakers'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)
