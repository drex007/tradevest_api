from django.core.mail import send_mail
from random import randint
from .models import CustomUser
from django.conf import settings

def send_otp_to_email(email_to):
    otp = randint(2356,9754)
    email_host = settings.EMAIL_HOST_USER

    subject= "Email verification from tradevest"
    message = f"Dear User, Your email verification Otp code is {otp}"
    send_mail(subject, message, email_host, [email_to])
    user = CustomUser.objects.filter(email=email_to).first()
    user.otp = otp
    user.save()