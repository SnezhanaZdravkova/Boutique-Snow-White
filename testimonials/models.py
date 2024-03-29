from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Service(models.Model):
    """ Service Model """
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Get url after superuser adds/edits service"""
        return reverse('services')


class Testimonial(models.Model):
    """ Testimonial Model """
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testimonials")
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='testimonial',
        null=True, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Testimonial: {self.service} by {self.name.username}"

    def get_absolute_url(self):
        """Get url after user adds/edits testimonial"""
        return reverse('testimonials')
