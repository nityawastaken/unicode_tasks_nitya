# bookings/serializers.py

from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'tour', 'booking_date', 'payment_method']
