from django.db import models
import uuid
from django.contrib.auth.models import User



class BaseModel(models.Model):# this model only acts as a parent class and because  the code abstrct is given true so the basemodel class is not saved in the abstract
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    class Meta:
        abstract = True
class UserAuthentication(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True,blank=True)
    is_admin = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    mobile_otp = models.CharField(max_length=5,null=True,blank=True)
    def __str__(self):
        return f'{self.user.first_name}==={self.id}==={self.is_driver}'
    
