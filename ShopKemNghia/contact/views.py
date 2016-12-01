from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.


def contact(request):
    title = 'Contact'
    form = ContactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data.get('name', None)
        comment = form.cleaned_data.get('comment', None)
        subject = 'Message from Son Site'
        message = '{user} {text}'.format(user=name,
                                         text=comment)
        from_email = form.cleaned_data.get('email', None)
        to_email = [settings.EMAIL_HOST_USER]
        send_mail(subject=subject,
                  message=message,
                  from_email=from_email,
                  recipient_list=to_email,
                  fail_silently=False)
        title = 'Thanks!'
        confirm_message = 'Thanks for the message, we will contact you soon!'
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message}

    template = 'contact.html'
    return render(request, template, context)
