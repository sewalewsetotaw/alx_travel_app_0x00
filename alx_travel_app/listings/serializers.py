# listings/serializers.py

from rest_framework import serializers
from .models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
    def validate(self, data):
        if data['check_out'] <= data['check_in']:
            raise serializers.ValidationError("Check-out date must be after check-in date.")
        return data
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
    def validate_rating(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value