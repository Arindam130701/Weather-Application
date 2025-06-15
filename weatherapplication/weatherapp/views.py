from django.shortcuts import render, HttpResponse
import requests
import datetime

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'kolkata'    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=90e1f30b91a7760eeec8225a9ec8539a'
    PARAMS = {
        'units': 'metric',
    }
    data = requests.get(url,PARAMS).json()


    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']

    day = datetime.date.today()
    return render(request, 'index.html', {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city,
    })