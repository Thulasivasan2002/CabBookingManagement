from rest_framework import serializers
from .models import *
from django.db import models

# class DriverValidationSerializer(serializers.Serializer):
#     # name = serializers.CharField(required = True)
#     contact_number = serializers.IntegerField(required = False)
#     email = serializers.EmailField(required = False)
#     license_number = serializers.CharField(required = False)
#     is_available = serializers.BooleanField(required = False)

class UserInfoValidationSerializer(serializers.Serializer):
    license_number = serializers.CharField(required = True)
    contact_number = serializers.IntegerField(required = True)
    email = serializers.EmailField(required = True)
    address = serializers.CharField(required = True) 
    
class CabValidationSerializer(serializers.Serializer):
    make = serializers.CharField(required = True)
    model = serializers.CharField(required = True)   
    year = serializers.IntegerField(default=0)
    registration_no = serializers.CharField(required = True)
    capacity = serializers.IntegerField(required = True)
    driver_info_id = serializers.UUIDField(required = True)
    
    
class BookingValidationSerializer(serializers.Serializer):
    date_booked = serializers.DateTimeField(required = True)
    start_location = serializers.CharField(required = True)
    end_location = serializers.CharField(required = True)
    start_time = serializers.TimeField(required = True)
    end_time = serializers.TimeField(required = True)    
    customer_info_id = serializers.UUIDField(required = True)
    cab_id = serializers.UUIDField(required = True)
       