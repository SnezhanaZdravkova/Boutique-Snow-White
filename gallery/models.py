from django.db import models
from django.urls import reverse
from testimonials.models import Service


class GalleryImages(models.Model):
    """ Model to show all work done in pictures """
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='all_pictures')
    image = models.ImageField(null=True, blank=False)

    def get_absolute_url(self):
        """Get url after user adds project image"""
        return reverse('project_images')

    def __str__(self):
        return self.service
