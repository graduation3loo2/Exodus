from rest_framework import serializers

from trips.models import Trips
from votes.models import Vote


class TripsSerializer(serializers.ModelSerializer):
    agency_name = serializers.ReadOnlyField(source='agency.name')

    class Meta:
        model = Trips
        fields = "__all__"


class VoteSerializer(serializers.ModelSerializer):
    agency_name = serializers.ReadOnlyField(source='agency.name')

    class Meta:
        model = Vote
        fields = "__all__"
