from django.urls import path
from . import views

urlpatterns = [
    path('', views.Services.as_view(), name='services'),
    path('testimonials/', views.Testimonials.as_view(), name='testimonials'),
    path(
        'testimonials/add/', views.AddTestimonial.as_view(),
        name='add_testimonial'
        ),
]
