from django.shortcuts import render
import requests
# Create your views here.


def home(request):
    # city="Kolkata"
    city=request.GET.get('city','Kolkata')
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d693f3dff6835e58b520256bf4e64afc'
    try:
        data = requests.get(url).json()
        payload = {
            'city': data.get('name', 'N/A'),
            'weather': data['weather'][0]['main'],
            'icon': data['weather'][0]['icon'],
            'kelvin_temperature': data['main']['temp'],
            'celsius_temperature': int(data['main']['temp'] - 273),
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
        }
    except (KeyError, IndexError):
        payload = {
            'city': 'N/A',
            'weather': 'N/A',
            'icon': 'N/A',
            'kelvin_temperature': 'N/A',
            'celsius_temperature': 'N/A',
            'pressure': 'N/A',
            'humidity': 'N/A',
            'description': 'N/A',
        }

    context={'data':payload}
    return render(request, 'home.html', context)