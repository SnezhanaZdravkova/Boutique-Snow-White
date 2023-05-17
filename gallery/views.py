from django.shortcuts import render
from django.views.generic import DeleteView, ListView, CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import GalleryImages
from .forms import AddImageForm


class ProjectImages(ListView):
    """ This view is used to display all photos """
    model = GalleryImages
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plain_message'] = True
        return context


class AddImage(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, CreateView):
    """ Admin can add Images from previous work """
    form_class = AddImageForm
    template_name = 'gallery/add_image.html'
    success_message = "Your image was added successfully"
    success_url = reverse_lazy('services')

    def test_func(self):
        """
       Ensure only superuser can add an image
        """
        if self.request.user.is_superuser:
            return True


class DeleteImage(
        LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete image view """
    model = GalleryImages
    template_name = 'gallery/delete_image.html'
    success_message = "Image successfully deleted"
    success_url = reverse_lazy('project_images')

    def test_func(self):
        """ Only superuser can delete an image """
        if self.request.user.is_superuser:
            return True
    
    def delete(self, request, *args, **kwargs):

        messages.success(self.request, self.success_message)
        return super(DeleteImage, self).delete(request, *args, **kwargs)
