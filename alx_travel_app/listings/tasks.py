
# listings/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(booking_id, user_email):
    """
    Sends an email to the user with the booking confirmation details.
    """
    subject = f"Booking Confirmation #{booking_id}"
    message = f"Thank you for your booking with ID {booking_id}. Your reservation is confirmed!"
    from_email = settings.DEFAULT_FROM_EMAIL

    send_mail(subject, message, from_email, [user_email])
