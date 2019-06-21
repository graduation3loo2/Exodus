from django.contrib import admin

# Register your models here.

from .models import Trips, TripPhotos, Activity

admin.site.register(Trips)
admin.site.register(TripPhotos)
admin.site.register(Activity)