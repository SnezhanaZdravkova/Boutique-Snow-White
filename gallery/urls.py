from django.urls import path
from .views import ProjectImages, AddImage


urlpatterns = [
    path('gallery/',
         ProjectImages.as_view(), name='project_images'),
    path('add_image/', AddImage.as_view(), name='add_image'),
]
