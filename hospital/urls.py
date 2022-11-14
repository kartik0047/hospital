from django.contrib import admin
from django.urls import path, include
from hospital.views import *
urlpatterns = [
    path('mapdetails/', MapDetails.as_view(), name='mapdetails'),
    path('notification/', Notification.as_view(), name='notification'),
    path('testSocket/', TestSocket.as_view(), name='testSocket'),
    path('send',send)
]
    
