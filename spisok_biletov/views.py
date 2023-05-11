from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Min, Max
from spisok_biletov.models import SpisokBiletov
from users.models import User
from spisok_biletov.forms import DefaultSearch, DataSearch, GorodSearch
from django.urls import reverse
# Create your views here.


def index(request):
    context = {
        'title': 'webcite',
        'login': User.objects.all(),
    }
    if request.method == 'POST':
        form = DefaultSearch(data=request.POST)
        if form.is_valid():
            date = request.POST['date']
            name_out = request.POST['name_out']
            name_in = request.POST['name_in']
            context.update({'bileti': SpisokBiletov.objects.filter(date=date, name_out=name_out, name_in=name_in)})
            context.update({'form': form})
    else:
        form = DefaultSearch()
        context.update({'bileti': SpisokBiletov.objects.all()})
        context.update({'form': form})
    return render(request, 'spisok_biletov/index.html', context)

def datapoisk(request):
    context = {
        'title': 'webcite',
    }
    if request.method == 'POST':
        form = DataSearch(data=request.POST)
        if form.is_valid():


            date = request.POST['date_2']

            context.update({'bileti': SpisokBiletov.objects.raw("SELECT * FROM spisok_biletov_spisokbiletov WHERE date = %s ORDER BY price LIMIT 1", [date])})
            context.update({'form': form})

    else:
        form = DataSearch()
        context.update({'bileti': SpisokBiletov.objects.all()})
        context.update({'form': form})
    return render(request, 'spisok_biletov/budzh.html', context)

#raw("SELECT * FROM spisok_biletov_spisokbiletov WHERE date = %s AND price = MIN(%s)", [date, price])
#.raw("SELECT * FROM spisok_biletov_spisokbiletov WHERE date = %s HAVING price = MIN(price) ORDER BY date", [date])})


def gorodpoisk(request):
    context = {
        'title': 'webcite',
    }
    if request.method == 'POST':
        form = GorodSearch(data=request.POST)
        if form.is_valid():
            name_out = request.POST['name_out_2']
            name_in = request.POST['name_in_2']
            context.update({'bileti': SpisokBiletov.objects.raw("SELECT * FROM spisok_biletov_spisokbiletov WHERE name_out = %s AND name_in = %s ORDER BY price DESC", [name_out, name_in])})
            context.update({'form': form})

    else:
        form = GorodSearch()
        context.update({'bileti': SpisokBiletov.objects.all()})
        context.update({'form': form})
    return render(request, 'spisok_biletov/dorog.html', context)


