from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProjectImages.as_view(), name='project_images'),
    path('gallery', views.AddImage.as_view(), name='add_image'),
]
