from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV

with open(BUS_STATION_CSV, encoding='utf-8', newline='\n') as csvfile:
    reader = csv.DictReader(csvfile)
    CONTENT = [row for row in reader]


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = request.GET.get('page', 1)
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
# получите текущую страницу и передайте ее в контекст
# также передайте в контекст список станций на странице
    context = {
        'page': page,
        'bus_stations': page.object_list,
    }
    return render(request, 'stations/index.html', context)









