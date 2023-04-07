from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.views import generic, View
from django.conf import settings
from django.template.loader import render_to_string

from .forms import ContactForm
from .models import Contact


class ContactView(View):
    """
    This view is used to display the contact form and
    handle GET and POST requests
    """

    def get(self, request):
        """
        Renders the contact form
        """
        if request.user.is_authenticated:
            form = ContactForm(initial={'email': request.user.email})
        else:
            form = ContactForm()

        return render(
            request,
            "contact/contact.html",
            {
                "contact_form": form,
            },
        )

    def post(self, request):

        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            cust_name = contact_form.instance.name
            cust_email = contact_form.instance.email
            subject = contact_form.instance.subject

            message = contact_form.instance.message
            message = render_to_string(
                'contact/confirmation_emails/confirmation_email_body.txt',
                {'cust_name': cust_name, 'message': message}
            )
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
            )
            contact_form.save()
            messages.success(self.request, 'Your enquiry has been sent')

            target = "home/index.html"
            context = {"plain_message": True}
        else:
            messages.error(request, """Form failed. Please ensure the
            form is valid """)
            target = "contact/contact.html"
            context = {
                "plain_message": True,
                "contact_form": contact_form
                }
        return render(request, target, context)
