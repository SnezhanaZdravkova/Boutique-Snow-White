from django.urls import path
from . import views

urlpatterns = [
    path('', views.Testimonials.as_view(), name='testimonials'),
    path('add/', views.AddTestimonial.as_view(), name='add_testimonial'),
    path('services/', views.Services.as_view(), name='services'),
    path('testimonials/add/', views.AddService.as_view(), name='add_services'),
    path('testimonials/edit/<int:pk>/', views.EditService.as_view(),
         name='edit_services'),
    path('testimonials/delete/<int:pk>/', views.DeleteService.as_view(),
         name='delete_services'),
    path('edit/<int:pk>/', views.EditTestimonial.as_view(),
         name='edit_testimonials'),
    path('delete/<int:pk>/', views.DeleteTestimonial.as_view(),
         name='delete_testimonials'),
]
