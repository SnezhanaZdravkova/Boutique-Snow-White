from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

from .forms import ContactForm


def contact(request):
    """
    Submits contact us form to the admin dashboard.
    """
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            subject = form.cleaned_data['subject'],
            message = form.cleaned_data['message'],
            form.save()

            send_mail({subject}, f'{name}, {email}, {message}',
                      settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER],
                      fail_silently=False)
            messages.success(request,
                             f'Thank you for Contacting Us.'
                             f'we will reply within 24 hrs!'
                             )

            return redirect(reverse('home'))
        else:
            messages.error(request,
                           f'Something went wrong with your Submission.'
                           f'Please try again.'
                           )

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
