from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def Trip(request):
    atrip = Trips.objects.get(trip_id=3)
    anagency = Agencies.objects.get(agency_id=atrip.agency_id)
    acomment = Comment.objects.get(trip_id=atrip.trip_id)
    areply = Reply.objects.all(comment_id=acomment.comment_id)
    auser = Users.objects.all(user_id=acomment.user_id)

    context = {
        'Ttrip': atrip,
        'Angency': anagency,
        'Comment': acomment,
        'Reply': areply,
        'User': auser,
    }
    return render(request, 'trip-page.html', context)
