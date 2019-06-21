from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import *


# Create your views here.
def User(request):
    auser = Users.objects.all(user_id=1)
    afollow= Follows.objects.all()
    atrip = Trips.objects.get()
    anagency = Agencies.objects.get()

    context = {
        'User': auser,
        'Ttrip': atrip,
        'Angency': anagency,
    }
    return render(request, 'user.html')
