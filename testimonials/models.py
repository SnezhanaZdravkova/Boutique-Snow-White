from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Service(models.Model):
    """ Model for Service """
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Get url after superuser adds/edits service"""
        return reverse('services')


class Testimonial(models.Model):
    """ Model for Testimonial """
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testimonials")
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='testimonial')
    body = models.TextField(max_length=1000, null=False, blank=False)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Testimonial: by {self.name}"

    def get_absolute_url(self):
        """Get url after user add/edit testimonial"""
        return reverse('testimonials')
