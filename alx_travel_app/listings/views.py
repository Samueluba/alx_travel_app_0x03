# listings/views.py

from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from .tasks import send_booking_confirmation_email
from rest_framework.response import Response

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        # Save the booking instance
        booking = serializer.save()

        # Trigger the email task asynchronously using delay
        send_booking_confirmation_email.delay(booking.id, booking.user.email)

        return Response(serializer.data)

