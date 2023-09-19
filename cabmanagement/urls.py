from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static



urlpatterns =[

    # path('welcomeMessage',views.welcomemessage,name='welcomeMessage'),
    # path('goodByeMessage',views.goodbyemessage,name='goodByeMessage'),
    # path('carsTheme/',views.theme,name='carsTheme'),
    # path('myModels/',views.getmodel,name='myModels'),
    # path('order/',views.orderer,name='order'),
    # path('searcher/',views.searchBooking,name='searcher/'),
    # path('customerListing/',views.listingValues,name='customerListing'),
    # path('firstCustomer/',views.firstValue,name='firstCustomer'),
    # path("deletingCustomer/",views.deletingCustomer,name='deletingcustomer'),
    # path('driverList/',views.getdrivers,name='driverList'),
    # path('getDrivers/',views.GetDrivers.as_view(),name='getDrivers'),
    # path('getCustomer/',views.GetCustomers.as_view(),name='getCustomer'),
    path('getCab/',views.GetCab.as_view(),name='getCab'),
    path('getBooking/',views.GetBookings.as_view(),name='getBooking'),
    # path('addDriver',views.AddDriver.as_view(),name='addDriver'),
    path('addCab/',views.AddCab.as_view(),name="addCab"),
    # path('addCustomer/',views.AddCustomer.as_view(),name = "addCustomer"),
    path("addBooking/",views.AddBooking.as_view(),name = "addBooking"),
    path('getUserInfo/',views.GetUserInfo.as_view(),name="getUserInfo/"),
    path('addUserInfo/',views.AddUserInfo.as_view(),name='addUserInfo'),
    path('getUserInfoDetails/',views.GetUserInfoDetails.as_view(),name='getUserInfoDetails/'),
    path('getCabDetails/',views.GetCabDetials.as_view(),name = 'getCabDetails/'),
    path('getBookingDetails/',views.GetBookingDetials.as_view(),name = 'getBookingDetails/'),
    path('speech-to-text/', views.speech_to_text, name='speech_to_text')
]