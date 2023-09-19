from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .res_serializer import *
from .request_serializers import *
from rest_framework import authentication,permissions

class GetTrips(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        data = request.data
        tripsq = Trip.objects.all()
        trip_serializer = TripSerializer(tripsq,many = True)
        return Response(trip_serializer.data)

class GetTripDetails(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        data = request.data
        # if 'total_distance' in data:
        #     tripsq = Trip.objects.get(total_distance = data['total_distance'])
        #     trip_serializer = TripSerializer(tripsq)
        #     return Response(trip_serializer.data)
        # if 'total_cost' in data:
        #     tripsq = Trip.objects.get(total_cost = data['total_cost'])
        #     trip_serializer = TripSerializer(tripsq)
        #     return Response(trip_serializer.data)
        if 'id' in data:
            tripsq = Trip.objects.get(id = data['id'])
            trip_serializer = TripSerializer(tripsq)
            return Response(trip_serializer.data)
        
        
        
    
class AddTrip(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        data = request.data
        validation = TripValidationSerializer(data = data)
        if validation.is_valid():
            if 'id' not in data:
                tripForm = {}
                tripForm['date_started'] =  data['date_started']
                tripForm['date_ended'] =  data['date_ended']   
                tripForm['total_distance'] =  data['total_distance']   
                tripForm['total_cost'] =  data['total_cost']   
                tripForm['is_completed'] =  data['is_completed']   
                tripForm['driver_id'] =  data['driver_id']   
                tripForm['cab_id'] =  data['cab_id']   
                tripForm['customer_id'] =  data['customer_id']   
                tripForm['booking_id'] =  data['booking_id']   
                Trip.objects.create(**tripForm)
                return Response({'message':'your trip detials have been saved'})
            else:
                trip = Trip.objects.get(id = data['id'])
                if 'date_started' in data:
                    trip.date_started = data['date_started']
                if 'date_ended' in data:
                    trip.date_ended = data['date_ended']    
                if 'total_distance' in data:
                    trip.total_distance = data['total_distance']  
                if 'total_cost' in data:
                    trip.total_cost = data['total_cost']
                if 'is_completed' in data:
                    trip.is_completed = data['is_completed']
                if 'driver_id' in data:
                    trip.driver_id = data['driver_id'] 
                if 'cab_id' in data:
                    trip.cab_id = data['cab_id']
                if 'customer_id' in data:
                    trip.customer_id = data['customer_id']
                if 'booking_id' in data:
                    trip.booking_id = data['booking_id']
                trip.save()
                return Response({"message":"Trip detials have been updated"})                             
        else:
            return Response({"Message":"Invalid Param"})          
    
class getReviews(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        data = request.data
        reviewsq = Review.objects.all()
        review_serializer = ReviewCabSerializer(reviewsq,many = True)
        return Response(review_serializer.data)   
    
class GetReviewDetials(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        data = request.data
        if 'customer_name' in data:
            reviewsq = Review.objects.get(customer_name = data['customer_name'])
            review_serializer = ReviewCabSerializer(reviewsq)
            return Response(review_serializer.data)      
        
class AddReview(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        data = request.data
        validation = ReviewValidationSerializer(data = data)
        if validation.is_valid():
            if 'id' not in data:
                reviewForm = {}
                reviewForm['customer_name'] = data['customer_name']
                reviewForm['review_text'] = data['review_text']    
                reviewForm['rating'] = data['rating']    
                reviewForm['date_posted'] = data['date_posted']    
                reviewForm['trip_id'] = data['trip_id']    
                cab_service_id = data['cab_service_id'] 
                review_initial_form = Review.objects.create(**reviewForm)   
                review_initial_form.cab_service.add(*cab_service_id)
                return Response({'message':'the review is saved'})
            else:
                review_detials_editor = Review.objects.get(id = data['id'])
                if 'customer_name' in data:
                    review_detials_editor.customer_name = data['customer_name']
                if 'review_text' in data:
                    review_detials_editor.review_text = data['review_text']
                if 'rating' in data:
                    review_detials_editor.rating = data['rating'] 
                if 'date_posted' in data:
                    review_detials_editor.date_posted = data['date_posted']
                if 'trip_id' in data:
                    review_detials_editor.trip_id = data['trip_id']
                if 'cab_service_id' in data:
                    review_detials_editor.cab_service.set(data['cab_service_id'])    
                review_detials_editor.save()
                return Response({"message":"your review have been edited"})
        else:
            return Response({"message" : "Invalid Params"})        