from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, ListView, CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Service, Testimonial
from .forms import ServiceForm, TestimonialForm


class Services(ListView):
    """ This view is used to display all services """
    model = Service
    template_name = 'testimonials/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plain_message'] = True
        return context


class Testimonials(ListView):
    """ This view is used to display all testimonials """
    model = Testimonial
    template_name = 'testimonials/testimonials.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plain_message'] = True
        return context


class AddTestimonial(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, CreateView):

    """This view is used to allow a user to add a testimonial"""
    form = TestimonialForm
    template_name = 'testimonials/add_testimonial.html'
    success_message = "Your testimonial was added successfully"

    def form_valid(self, form):
        """
        Override the form_valid() method in model form view
        in order to set the signed in user as the name on the testimonial.
        """
        form.instance.name = self.request.user
        return super().form_valid(form)
