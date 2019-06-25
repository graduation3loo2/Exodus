from rest_framework import viewsets

# Create your views here.
from api.serializer import TripsSerializer, VoteSerializer
from trips.models import Trips
from votes.models import Vote


class TripsViewSet(viewsets.ModelViewSet):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer



class VotesViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

