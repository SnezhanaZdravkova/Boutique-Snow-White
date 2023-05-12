from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, ListView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Service, Testimonial

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
