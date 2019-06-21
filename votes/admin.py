from django.contrib import admin

# Register your models here
from .models import Vote, Response, Users

admin.site.register(Vote)
admin.site.register(Response)
admin.site.register(Users)
