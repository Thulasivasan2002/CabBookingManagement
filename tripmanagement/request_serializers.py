from rest_framework import serializers


class TripValidationSerializer(serializers.Serializer):
    date_started = serializers.DateField(required = True)
    date_ended = serializers.DateField(required = True)
    total_distance = serializers.IntegerField(required = True)
    total_cost = serializers.IntegerField(required = True)
    is_completed = serializers.BooleanField(required = True)
    driver_id = serializers.UUIDField(required = True)
    cab_id = serializers.UUIDField(required = True)
    customer_id = serializers.UUIDField(required = True)
    booking_id = serializers.UUIDField(required = True)

class ReviewValidationSerializer(serializers.Serializer):
    customer_name = serializers.CharField(required = True)
    review_text = serializers.CharField(required = True)
    rating = serializers.IntegerField(required = True)
    date_posted = serializers.DateField(required = True)
    trip_id = serializers.UUIDField(required = True)
    # cab_service_id  = serializers.ListField(child = serializers.IntegerField(),allow_empty = False)
    # def validate_cab_service_id(self, value):
    #     if len(value) < 4:
    #         raise serializers.ValidationError("You must select at least 2 tags for an article.")
    #     return value
        