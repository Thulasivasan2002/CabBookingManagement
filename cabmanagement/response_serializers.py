from rest_framework import serializers
from . models import *
# this file is created so that the code can convert the db values('unreadable') into the json values('redable')


# class DriverSerializer(serializers.ModelSerializer):#after reciving the values from its corresponded view class it will change the db values to the json.
#     # photo = serializers.SerializerMethodField()
#     first_name = serializers.SerializerMethodField()

    # class Meta:# while creating a serializer this 'class Meta' is must.
        # model = Driver#this model is the one that tells which class in the model table should the code read.
        # fields = ['first_name','contact_number']#fields its very important because its the variable thaat shows which values can be shown as json.
    # def get_photo(self, obj):
    #     return obj.photo.url
    # def get_first_name(self,obj):
    #     return obj.user.first_name

    
        
            

        
class UserInfoSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    class Meta:
        model = UserInfo
        fields = ['id','first_name','contact_number','email']   
    def get_first_name(self,obj):
        return obj.user.first_name
    def get_email(self,obj):
        return obj.user.email     
        
class CabSerializer(serializers.ModelSerializer):
    driver_detials = serializers.SerializerMethodField()
    class Meta:
        model = Cab
        fields = ['id','make','model','year','driver_detials']
        
    def get_driver_detials(self,obj):
        try:
            return {"name":obj.driver_info.user.first_name,"contact_number":obj.driver_info.contact_number}
        except:
            return None    
        
class BookingSerializer(serializers.ModelSerializer):
    customer_detials = serializers.SerializerMethodField()#if you'r table contains foriegn key 
    cab_detials = serializers.SerializerMethodField()
    class Meta:
        model = Booking
        fields = ['date_booked','customer_detials','cab_detials']
    def get_customer_detials(self,obj):#to get customer_detials variable for the foriegn key in our table
        return {"name":obj.customer_info.user.first_name,"email":obj.customer_info.user.email}# if you are going to get more then two values in foriegn key we should use it  like this.    
    def get_cab_detials(self,obj):
        return {"make":obj.cab.make,"registration_no":obj.cab.registration_no}    
                
        