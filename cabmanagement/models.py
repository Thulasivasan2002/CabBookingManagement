from django.db import models
import uuid
from django.contrib.auth.models import User
from authentication.models import *

# from .models import Cab


class UserInfo(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null = True,blank=True)
    user_authentication = models.ForeignKey(UserAuthentication,on_delete = models.SET_NULL,null=True,blank=True)
    # name = models.CharField(max_length=100,null=True,blank=True)
    contact_number = models.CharField(max_length=10,null=True,blank=True)
    # email = models.EmailField(max_length=250,null=True,blank=True)
    license_number = models.CharField(max_length=100,null=True,blank=True)
    is_available = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='driver_img')
    address = models.TextField(null=True,blank=True) 

         
    def __str__(self):
        return str(self.id)+"==="+self.user.first_name+"==="+str(self.is_available) # f'{self.id}==={self.name}'
    
class Cab(BaseModel):
    make = models.CharField(max_length=200,null=True,blank=True)
    model = models.CharField(max_length=200,null=True,blank=True)   
    year = models.IntegerField(default=0)
    registration_no = models.CharField(max_length=200,null=True,blank=True)
    capacity = models.IntegerField(default=0)
    driver_info = models.ForeignKey(UserInfo,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return str(self.id)+"==="+self.model+"==="+self.driver_info.user.first_name#this str function acts as the table name in the in our django admin site.
    
# class Customer(BaseModel):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
#     # name = models.CharField(max_length=200,blank=True,null=True)
#     contact_number = models.CharField(max_length=10,blank=True,null=True)
#     # email = models.EmailField(max_length=100,null=True,blank=True)
#     address = models.TextField(null=True,blank=True) 

#     def __str__(self):
#         return str(self.id)+"==="
       
class Booking(BaseModel):
    date_booked = models.DateTimeField(null=True,blank=True)
    start_location = models.CharField(max_length=200,null=True,blank=True)
    end_location = models.CharField(max_length=200,null=True,blank=True)
    start_time = models.TimeField(null=True,blank=True)
    end_time = models.TimeField(null=True,blank=True)
    customer_info = models.ForeignKey(UserInfo,on_delete=models.SET_NULL,null=True,blank=True)
    cab = models.ForeignKey(Cab,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return str(self.id)+"==="+str(self.start_location)+"==="+self.customer_info.user.first_name

