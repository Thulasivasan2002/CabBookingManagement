from django.shortcuts import render
# from google.cloud import speech
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.template import loader
from .models import *
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from . response_serializers import *
from.request_serializers import *
from django.core.files.base import ContentFile
import base64
import random
from rest_framework import authentication,permissions
from rest_framework.authtoken.models import Token
from authentication.utils import *

# def welcomeMessage(request):
#     return HttpResponse('welcome home guys')

# def goodbyeMessage(request):
#     return HttpResponse('see you later')

# def theme(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())



# def getdrivers(request):
#     alldrivers = Driver.objects.all()
#     template = loader.get_template('drivers.html')
#     context = {
#         'alldrivers' : alldrivers,
#     }
#     return HttpResponse(template.render(context,request))

# def getmodel(request):
#     models = Cab.objects.filter(year__gt=2000)
#     template = loader.get6_template('cab.html')
#     context = {
#         'models':models
#     }
#     return HttpResponse(template.render(context,request))

# def searchBooking(request):
#         booked = Booking.objects.get(customer__name ='thulasivasan s')
#         template = loader.get_template('bookingSearch.html')
#         context = {
#         'booked': booked
#             }
#         return HttpResponse(template.render(context,request))


# def orderer(request):
#     customers = Customer.objects.order_by('name')
#     customer = Customer.objects.order_by('-name')
#     excluder = Customer.objects.exclude(name = 'naresh D')
#     Quser = Customer.objects.filter(Q(name = 'thulasiivasan s')|Q(name = 'naresh D'))
#     template = loader.get_template('orderTemp.html')
#     context = {
#         'customers': customers,
#         'customer' : customer,
#         'excluder' : excluder,
#         'Quser': Quser
#     }
#     return HttpResponse(template.render(context,request))

# def listingValues(request):
#     listing = Customer.objects.values_list('name',flat=True)
#     template = loader.get_template('valueList.html')
#     context = {
#         'listing' : listing
#     } 
#     return HttpResponse(template.render(context,request))

# def firstValue(request):
#     first_value= Customer.objects.last()
#     last_value = Customer.objects.first()
#     template = loader.get_template('firstlast.html')
#     context = {
#         'fvalue' : first_value,
#         'lvalue' : last_value
#     } 
#     return HttpResponse(template.render(context,request))

# def deletingCustomer(request):
#     nameDeleting = Customer.objects.filter(name='thulasivasan s').delete()
#     template = loader.get_template('deletevalues.html')
#     context = {
#         'deletingCustomer' :nameDeleting
#     }
#     return HttpResponse(template.render(context,request))

# class GetDrivers(APIView):# the work od this class is to convert the un redable db values in to json values using the serializers we have created
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     def post(self,request):
#         data = request.data
#         # driversQ = Driver.objects.all()
#         driversQ = Driver.objects.filter(id= data['id'])
#         serializer = DriverSerializer(driversQ ,many=True)# this seerializer sends the driver query to the driver serializer
#         return Response(serializer.data)
    
# class AddDriver(APIView):
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     def post(self,request):
#         data = request.data
#         print('datdatdatdtadt',data)
#         validation = DriverValidationSerializer(data = data)
#         if validation.is_valid():
#             if 'id' not in data:
#                 if User.objects.filter(email = data['email']).count()== 0:
#                     user = User.objects.create(username=data['email'],password= data['password'],email=data['email'])
#                     user.first_name = data['first_name']
#                     user.last_name = data['last_name']
#                     user.save()
#                     driverForm = {}
#                     # driverForm['name'] = data['name']
#                     driverForm['contact_number'] =data['contact_number']
#                     # driverForm['email'] =data['email']
#                     driverForm['license_number'] =data['license_number']
#                     driverForm['is_available'] =data['is_available']
#                     if 'photo' in data:
#                         image_data  = ContentFile(base64.b64decode(data['photo']))
#                         file_name  =  str(random.randint(111111,999999))+'.jpg'
                
#                     driver = Driver.objects.create(user = user ,**driverForm)
#                     driver.photo.save(file_name,image_data,save = True)
#                     # driver.photo.save(file_name,image_data,save = True)
#                     return Response({'Message:Driver added successfully'})
#                 else:
#                     return Response({'messgae':'email alredy exist'})      
                        
#             else:
#                 driver = Driver.objects.get(id = data['id'])
#                 if 'first_name' in data:
#                     driver.user.first_name = data['first_name']
#                     driver.user.save()
#                 if 'last_name' in data:
#                     driver.user.last_name = data['last_name']
#                     driver.user.save()
#                 if 'contact_number' in data:
#                     driver.contact_number = data['contact_number']
#                 if 'email' in data:
#                     driver.email = data['email']        
#                 if 'license_number' in data:
#                     driver.license_number = data['license_number']
#                 if 'is_available' in data:
#                     driver.is_available = data['is_available']
#                 if 'photo' in data:
#                     image_data = ContentFile(base64.b64decode(data['photo']))
#                     file_name = str(random.randint(111111,999999))+'.jpg'    
#                     driver.photo.save(file_name,image_data,save = True)
#                 driver.save()    
                
#                 return Response({'Message':'driver detials have been updated'}) 
#         else:
#             return Response({'Message':'Invalid Params'})       
         
    
class GetUserInfo(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        data = request.data
        #customersq = Customer.objects.filter(name = data['name'])
        #customersq = Customer.objects.filter(name__contains = data['name'])
        usersq = UserInfo.objects.all()
        if 'is_customer' in data:
            usersq = UserInfo.objects.filter(user_authentication__is_customer = data['is_customer'])
        if 'is_driver' in data:    
            usersq = UserInfo.objects.filter(user_authentication__is_driver = data['is_driver'])
        driver_serializer = UserInfoSerializer(usersq , many=True)
        return Response(driver_serializer.data)
        
class GetUserInfoDetails(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        data = request.data
        if 'id' in data:
            userq = UserInfo.objects.get(id = data['id'])
            userSerializer = UserInfoSerializer(userq)
            return Response(userSerializer.data)
        # if 'first_name' in data:
        #     userq = UserInfo.objects.get(user__first_name = data['first_name'])    
        #     userSerializer = UserInfoSerializer(userq)
        #     return Response(userSerializer.data)
              

class AddUserInfo(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        data = request.data
        validation = UserInfoValidationSerializer(data = data)
        if validation.is_valid():
            if 'id' not in data:
                if User.objects.filter(email = data['email']).count() == 0:
                    user = User.objects.create(username = data['email'],password = data['password'],email = data['email'],first_name = data['first_name'],last_name = data['last_name'])
                    # token = Token.objects.create(user=user)
                    token = get_token_by_user(user)
                    user_authentication = UserAuthentication.objects.create(user = user)
                    if 'is_admin' in data:
                        user_authentication.is_admin = data['is_admin']
                    if 'is_customer' in data:
                        user_authentication.is_customer = data['is_customer']
                    if'is_driver' in data:
                        user_authentication.is_driver = data['is_driver']
                    if 'is_employee' in data:
                        user_authentication.is_employee = data['is_employee']
                    if 'otp' in data:
                        user_authentication.mobile_otp = data['otp']
                            
                    user_authentication.save()    
                    userInfoForm = {}
                    if 'is_driver' in data:
                        userInfoForm['license_number'] = data['license_number']
                        userInfoForm['is_available'] = data['is_available']
                    userInfoForm['contact_number'] = data['contact_number']
                    userInfoForm['address'] = data['address']
                    if 'photo' in data:
                        image_data  = ContentFile(base64.b64decode(data['photo']))
                        file_name  =  str(random.randint(111111,999999))+'.jpg'
                
                    user_info = UserInfo.objects.create(user=user,user_authentication=user_authentication,**userInfoForm)
                    user_info.photo.save(file_name,image_data,save = True)
                    
                    return Response({'Message':'new User is added'})
                else:
                    return Response({'Message':'User email exist create different one'})
            else:
                user_info_detials_editor = UserInfo.objects.get(id = data['id']) 
                if 'first_name' in data:
                    user_info_detials_editor.user.first_name = data['first_name']
                    user_info_detials_editor.user.save()
                if 'last_name' in data:
                    user_info_detials_editor.user.last_name = data['last_name']        
                    user_info_detials_editor.user.save()
                if 'license_number' in data:
                    user_info_detials_editor.license_number = data['license_number'] 
                if 'contact_number' in data:
                    user_info_detials_editor.contact_number = data['contact_number']
                if  'is_available' in data:
                    user_info_detials_editor.is_available = data['is_available'] 
                if 'address' in data:
                    user_info_detials_editor.address = data['address']
                if 'photo' in data:
                    image_data = ContentFile(base64.b64decode(data['photo']))
                    file_name = str(random.randint(111111,999999))+'.jpg'    
                    user_info_detials_editor.photo.save(file_name,image_data,save = True)
                        
                user_info_detials_editor.save()
                return Response({'Message':'your User Information as been edited'})             
                       
        else:
            return Response({'Message':'Invalid Params'})
            
            
          
        
class GetCab(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self,request):
        data = request.data
        print('data',data)
        # cabq = Cab.objects.filter(capacity = data['capacity'])
        # cabq = Cab.objects.filter(capacity__in = data['capacity'])
        # cabq = Cab.objects.filter(capacity__gte = data['capacity'])
        # cabq = Cab.objects.filter(capacity__lte = data['capacity'])
        # cabq = Cab.objects.filter(capacity__lt = data['capacity'])
        # cabq = Cab.objects.filter(make__startswith = data['make'])
        # cabq = Cab.objects.filter(make__istartswith = data['make'])
        # cabq = Cab.objects.filter(make__iendswith = data['make'])
        cabq = Cab.objects.all()
        if 'q' in data:
            cabq = Cab.objects.filter(model__icontains = data['q'])
        
        cab_serializer = CabSerializer(cabq,many = True)
        return Response(cab_serializer.data)    
    
class GetCabDetials(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        data = request.data
        if 'id' in data:
            cabq = Cab.objects.get(id = data['id'])
            cabDetialsSerializer = CabSerializer(cabq)
            return Response(cabDetialsSerializer.data)
        # if 'model' in data:
        #     cabq = Cab.objects.get(model = data['model'])
        #     cabDetialsSerializer = CabSerializer(cabq)
        #     return Response(cabDetialsSerializer.data)
        # if 'capacity' in data:
        #     cabq = Cab.objects.get(capacity = data['capacity'])    
        #     cabDetialsSerializer = CabSerializer(cabq)
        #     return Response(cabDetialsSerializer.data)
        
         

class AddCab(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        data = request.data
        validation = CabValidationSerializer(data = data)
        if validation.is_valid():
            if 'id' not in data:
                if Cab.objects.filter(registration_no = data['registration_no']).count() == 0:
                    cabForm = {}
                    cabForm['make'] = data['make']
                    cabForm['model'] = data['model']
                    cabForm['year'] = data['year']
                    cabForm['registration_no'] = data['registration_no']
                    cabForm['capacity'] = data['capacity']
                    cabForm['driver_info_id'] = data['driver_info_id']
                    
                    Cab.objects.create(**cabForm)
                    return Response({'Message':'The Cab is added'})
                else:
                    return Response({'Message':'the cab is already added check the registration number'})        
            else:
                cab = Cab.objects.get(id = data['id'])
                if 'make' in data:
                    cab.make = data['make']
                if 'model' in data:    
                    cab.model = data['model']
                if'year' in data:    
                    cab.year = data['year']
                if 'registration_no' in data:    
                    cab.registration_no = data['registration_no']
                if 'capacity' in data:    
                    cab.capacity= data['capacity']
                if 'driver_info_id' in data:   
                    cab.driver_info_id = data['driver_info_id']
                cab.save()    
                return Response({'Message':'your cab detials have been edited'})
        else:
            return Response({"Message":"Invalid Param"})
            
class GetBookings(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        data = request.data
        bookingq = Booking.objects.all()
        if 'q' in data:
            bookingq = Booking.objects.filter(date_booked__iscontains = data['q'])
        book_serializer = BookingSerializer(bookingq,many=True)
        return Response(book_serializer.data)    
class GetBookingDetials(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        data = request.data
       
        if 'id' in data:
            bookingq = Booking.objects.get(id = data['id'])
            booking_serializer = BookingSerializer(bookingq)
            return Response(booking_serializer.data)
        
        

class AddBooking(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        data = request.data
        validation = BookingValidationSerializer(data = data) 
        if validation.is_valid():
            if 'id' not in data:
                bookingForm = {}
                bookingForm['date_booked'] = data['date_booked']
                bookingForm['start_location'] = data['start_location']
                bookingForm['end_location'] = data['end_location']
                bookingForm['start_time'] = data['start_time']
                bookingForm['end_time'] = data['end_time']
                bookingForm['customer_info_id'] = data['customer_info_id']
                bookingForm['cab_id'] = data['cab_id']
                Booking.objects.create(**bookingForm)
                return Response({'Message':'Booking completed'})
            else:
                booking = Booking.objects.get(id = data['id'])
                if 'date_booked' in data:
                    booking.date_booked = data['date_booked']
                if 'start_location' in data:    
                    booking.start_location = data['start_location']
                if 'end_location' in data:    
                    booking.end_location=data['end_location']
                if 'start_time' in data:    
                    booking.start_time = data['start_time']
                if 'end_time' in data:    
                    booking.end_time = data['end_time']
                if 'customer_info_id' in data:    
                    booking.customer_info_id = data['customer_info_id']
                if ' cab_id' in data:    
                    booking.cab_id = data['cab_id']
                booking.save()
                return Response({'Message':'you have updated your booking detials'})
        else:
            return Response({"Message":"Invalid Params"})    
     

def speech_to_text(request):
    if request.method == 'POST':
        audio_file = request.FILES['audio_file']
        client = speech.SpeechClient()

        with audio_file.open('rb') as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code='en-US',
        )

        response = client.recognize(config=config, audio=audio)

        # Process the response and extract the transcribed text
        transcripts = [result.alternatives[0].transcript for result in response.results]

        return render(request, 'speech_to_text.html', {'transcripts': transcripts})


