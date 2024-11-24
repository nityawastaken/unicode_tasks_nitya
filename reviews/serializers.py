# reviews/serializers.py

from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'tour', 'rating', 'comment', 'review_date']
