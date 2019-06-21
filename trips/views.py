from django.shortcuts import render

from .models import Trips, Agencies, Activity
from .forms import SearchForm
from django.db.models import Q
from django.utils.timezone import make_aware
from django.conf import settings



def trips(request):

    agencies = Agencies.objects.all()
    trips = Trips.objects.all()
    form = SearchForm()

    if request.method == 'GET':
        if request.GET.get('form'):
            form = SearchForm(request.GET)
            if form.is_valid():
                city = form.cleaned_data['Destination']
                date_from = form.cleaned_data['Date']
                date_to = form.cleaned_data['Date2']
                duration_from = form.cleaned_data['duration_in_days']
                duration_to = form.cleaned_data['duration_in_days2']
                price_start = form.cleaned_data['price']
                price_end = form.cleaned_data['price2']
                meals = form.cleaned_data['meals']
                agency = form.cleaned_data['agency']
                filters = []
                if agency != '':
                    agencyiesIDS = Agencies.objects.filter(name__icontains=agency)
                    ids = []
                    for agencyID in agencyiesIDS:
                        idd = agencyID.agency_id
                        ids.append(idd)
                    agencyfilter = Trips.objects.filter(agency_id__in=ids)
                    filters.append(agencyfilter)
                if date_from is not None and date_to is not None:
                    datefilter = Trips.objects.filter(Q(date_from__gte=date_from) & Q(date_to__lte=date_to))
                    filters.append(datefilter)
                elif date_from is not None:
                    date_fromfilter = Trips.objects.filter(date_from__gte=date_from)
                    filters.append(date_fromfilter)
                elif date_to is not None:
                    date_tofilter = Trips.objects.filter(date_to__lte=date_to)
                    filters.append(date_tofilter)
                if price_start is not None and price_end is not None:
                    pricefilter = Trips.objects.filter(Q(price__gte=price_start) & Q(price__lte=price_end))
                    filters.append(pricefilter)

                elif price_start is not None:
                    price_startfilter = Trips.objects.filter(price__gte=price_start)
                    filters.append(price_startfilter)
                elif price_end is not None:
                    price_endfilter = Trips.objects.filter(price__lte=price_end)
                    filters.append(price_endfilter)

                if city is not '':
                    cityfilter = Trips.objects.filter(to_location__icontains=city)
                    filters.append(cityfilter)
                if meals in ['fullboard', 'halfboard']:
                    mealfilter=Trips.objects.filter(meals__exact=meals)
                    filters.append(mealfilter)
                if len(filters) > 0:
                    trips = filters[0]
                    for Filter in filters:
                        trips = trips | Filter

                context = {
                    'trips': trips,
                    'agencies': agencies,
                    'form': form,
                }
                return render(request, 'trips.html', context)
    if request.POST.get('select', None):
        sort_option = request.POST.get('select')
        trips = trips.order_by(sort_option)

        context = {
            'trips': trips,
            'agencies': agencies,
            'form': form,
        }
        return render(request, 'trips.html', context)
    else:
        context = {
            'trips': trips,
            'agencies': agencies,
            'form': form,
        }
        return render(request, 'trips.html', context)