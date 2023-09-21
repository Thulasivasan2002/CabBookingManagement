from django.db import models
import uuid
from cabmanagement.models import *
from authentication.models import *


class Trip(BaseModel):
    date_started = models.DateField(null= True,blank=True)
    date_ended = models.DateField(null= True,blank=True)
    total_distance = models.IntegerField(default=0,null=True,blank=True)
    total_cost = models.IntegerField(default=0,null=True,blank=True)
    is_completed = models.BooleanField(default=True)
    driver = models.ForeignKey(UserInfo,related_name='driver_info',on_delete=models.SET_NULL,blank=True,null=True)
    cab = models.ForeignKey(Cab,on_delete=models.SET_NULL,blank=True,null=True)
    customer = models.ForeignKey(UserInfo,related_name='customer_info',on_delete=models.SET_NULL,blank=True,null=True)
    booking = models.ForeignKey(Booking,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
            return str(self.id)+"==="+self.customer.user.first_name


    
class Review(BaseModel):
    customer_name = models.CharField(max_length=200,blank=True,null=True)
    review_text = models.TextField(null=True,blank=True)
    rating = models.IntegerField(default=1,null=True,blank=True)
    date_posted = models.DateField(null=True,blank=True)
    trip = models.ForeignKey(Trip,on_delete=models.SET_NULL,null=True,blank=True) 
    cab_service = models.ManyToManyField(Cab)   

    def __str__(self):
        return str(self.id)+"==="+self.customer_name

