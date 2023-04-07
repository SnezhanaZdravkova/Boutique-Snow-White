from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """ Model for contact us """

    name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000, default='')
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_on']
