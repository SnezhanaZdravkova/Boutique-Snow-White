from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
    # path('', views.ContactView.as_view(), name='contact'),
]
