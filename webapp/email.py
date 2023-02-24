import traceback

from django.conf import settings
from django.core.mail import send_mail


def send_email(subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=["amanr.ic18@nsut.ac.in"],
        fail_silently=False,
    )


def send_email_on_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:

            send_email(
                subject=f"Ticket Booking Error: {e}",
                message=(
                    "Unable to consume the API due to the following error:"
                    "\n\n"
                    f"{traceback.format_exc()}"
                ),
            )
        raise

    return wrapper
