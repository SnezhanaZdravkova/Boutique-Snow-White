from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Service(models.Model):
    """ Service Model """
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    """ Testimonial Model """
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testimonials")
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='testimonial')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Testimonial: {self.service} by {self.name.username}"

@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """Create or update the user profile"""
    if created:
        Profile.objects.create(user=instance)