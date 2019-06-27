from rest_framework import serializers

from trips.models import Trips
from user.models import Follows
from votes.models import Vote, Response


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


class ResponseSerializer(serializers.ModelSerializer):
    vote = VoteSerializer(many=False)

    class Meta:
        model = Response
        fields = "__all__"


class FollowsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follows
        fields = "__all__"
