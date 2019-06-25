from rest_framework import serializers

from trips.models import Trips


class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = ('trip_id', 'agency_id', 'name', 'from_location', 'to_location', 'date_from', 'date_to', 'meals', 'deadline', 'price', 'description', 'views', 'rate')