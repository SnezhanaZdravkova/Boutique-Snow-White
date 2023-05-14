from django.contrib import admin
from .models import GalleryImages


class ProjectImagesAdmin(admin.ModelAdmin):
    """Allows admin to manage all images via the admin panel"""
    list_display = (
        'service',
        'image',
    )


admin.site.register(GalleryImages, ProjectImagesAdmin)
