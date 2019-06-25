
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import TripsViewSet


router = routers.DefaultRouter()
router.register(r'trips', TripsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('agencies/', include('agencies.urls')),
    path('', include('home.urls')),
    path('trips/', include('trips.urls')),
    path('votes/', include('votes.urls')),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),

]
