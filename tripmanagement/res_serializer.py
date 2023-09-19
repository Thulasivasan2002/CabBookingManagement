from rest_framework import serializers#imported serializers from the 'rest_framework'
from tripmanagement.models import *#both line2,3 imports the models from the two apps i have created in this project
from cabmanagement.models import *

class TripSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()
    cab_made_in = serializers.SerializerMethodField()
    driver_name = serializers.SerializerMethodField()
    booking_contact_number = serializers.SerializerMethodField()
    class Meta:
        model = Trip
        fields = ["customer_name","date_started","date_ended","total_distance","total_cost","cab_made_in","booking_contact_number","driver_name"] #"customer_name","driver_name","booking_contact_number"
    def get_customer_name(self,obj):
        return obj.customer.user.first_name   
    def get_cab_made_in(self,obj):
        return obj.cab.make
    def get_driver_name(self,obj):
        return obj.driver.user.first_name
    def get_booking_contact_number(self,obj):
        return obj.booking.customer_info.contact_number
        
class ReviewSerializer(serializers.ModelSerializer):
    # booking_detials = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = ["customer_name","review_text","rating"]#"booking_detials"
    # def get_booking_detials(self,obj):
    #     return obj.trip.booking.customer.contact_number          
        
# class ReviewCabSerializer(serializers.ModelSerializer):
#     cab_details = serializers.SerializerMethodField()
#     class Meta:
#         model = Review    
#         fields = ["cab_details"]    
#     def get_cab_details(self,obj):
#         cab =[]
#         for x in obj.cab_service.all():
#             cab.append({"model":x.model,"year":x.year})
#         return cab
    
class ReviewCabSerializer(serializers.ModelSerializer):
    cab_detials = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = ["customer_name","review_text","rating","cab_detials","customer_name"]
    def get_cab_detials(self,obj):#this is a get function for many to many table
        cab = []
        for i in obj.cab_service.all():
            cab.append({"model":i.model,"make":i.make,"year":i.year})  
        return cab          
                
            
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        