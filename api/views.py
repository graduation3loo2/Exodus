from rest_framework import viewsets

# Create your views here.
from api.serializer import TripsSerializer, VoteSerializer, ResponseSerializer, FollowsSerializer
from trips.models import Trips
from votes.models import Vote, Response
from user.models import Follows


class TripsViewSet(viewsets.ModelViewSet):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer


class VotesViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follows.objects.all()
    serializer_class = FollowsSerializer
