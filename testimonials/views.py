from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView, ListView, CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Service, Testimonial
from .forms import ServiceForm, TestimonialForm
from django.urls import reverse_lazy


class Services(ListView):
    """ This view is used to display all services """
    model = Service
    template_name = 'testimonials/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plain_message'] = True
        return context


class AddService(
        LoginRequiredMixin,
        SuccessMessageMixin, CreateView):

    """This view is used to allow site owner to add a new service"""

    model = Service
    form_class = ServiceForm
    template_name = 'testimonials/add_services.html'
    success_message = "%(calculated_field)s was created successfully"

    def get_success_message(self, cleaned_data):
        """
        This function overrides the get_success_message() method to add
        the service name into the success message.
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.name,
        )

    def test_func(self):
        """ only superuser can add serivces """

        if self.request.user.is_superuser:
            return True


class EditService(UpdateView):
    """ View to allow superuser to update services """
    model = Service
    form_class = ServiceForm
    template_name = 'testimonials/edit_services.html'
    success_message = "%(calculated_field)s was edited successfully"

    def test_func(self):
        """ Only superuser can edit service details """
        if self.request.user.is_superuser:
            return True

    def get_success_message(self, cleaned_data):
        """
        Override the get_success_message() method to add the service name
        into the success message.
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.name,
        )


class DeleteService(
        LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ The superuser only can delete a service """
    model = Service
    template_name = 'testimonials/delete_services.html'
    success_message = "Service deleted successfully"
    success_url = reverse_lazy('services')

    def test_func(self):
        """ Only superuser can delete service details """
        if self.request.user.is_superuser:
            return True

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display sucess message given
        SucessMessageMixin cannot be used in generic.DeleteView.
        Credit: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        messages.success(self.request, self.success_message)
        return super(DeleteService, self).delete(request, *args, **kwargs)


class Testimonials(ListView):
    """ This view is used to display all testimonials """
    model = Testimonial
    template_name = 'testimonials/testimonials.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plain_message'] = True
        return context


class AddTestimonial(
        LoginRequiredMixin,
        SuccessMessageMixin, CreateView):

    """This view is used to allow a user to add a testimonial"""
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'testimonials/add_testimonial.html'
    success_message = "Your testimonial was added successfully"

    def form_valid(self, form):
        """
        Override the form_valid() method in model form view
        in order to set the signed in user as the name on the testimonial.
        """
        form.instance.name = self.request.user
        return super().form_valid(form)
