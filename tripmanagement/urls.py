from django.urls import path
from . import views

urlpatterns =[
    path('getTrip/',views.GetTrips.as_view(),name='getTrip'),
    path('getReview/',views.getReviews.as_view(),name= 'getReview'),
    path('addTrip/',views.AddTrip.as_view(),name = 'addTrip'),
    path('addReview/',views.AddReview.as_view(),name = 'addReview'),
    path('getTripDetails/',views.GetTripDetails.as_view(),name='getTripDetials/'),
    path('getReviewDetails/',views.GetReviewDetials.as_view(),name='getReviewDetails')
    
]