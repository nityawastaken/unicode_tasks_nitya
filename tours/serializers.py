# tours/serializers.py

from rest_framework import serializers
from .models import Tour

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['id', 'name', 'category', 'dates', 'capacity', 'location', 'price']
