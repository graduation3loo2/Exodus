from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from api.serializer import TripsSerializer
from trips.models import Agencies, Trips, TripPhotos,Users, Activity


class TripsViewSet(viewsets.ModelViewSet):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer
