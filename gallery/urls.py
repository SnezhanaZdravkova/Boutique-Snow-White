from django.urls import path
from .views import ProjectImages, AddImage, DeleteImage


urlpatterns = [
    path('gallery/',
         ProjectImages.as_view(), name='project_images'),
    path('add_image/', AddImage.as_view(), name='add_image'),
    path('gallery/delete/<int:pk>/', DeleteImage.as_view(),
        name='delete_image'),
]
