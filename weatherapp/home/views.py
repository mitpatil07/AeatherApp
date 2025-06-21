from django.shortcuts import render
import datetime
import requests

def home(request):
    
    error_message = None  # To show error in template

    if 'city' in request.POST:
        city = request.POST['city'].strip().title()

        if not city:
            error_message = "Please enter a city name."
            city = 'mumbai'  # Optionally, you can choose to not call API if empty
    else:
        city = 'Mumbai'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f125e9be2a005e234924c43ab459da12'
    parameter = {'units': 'metric'}


    data = requests.get(url,parameter).json()

    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']
    day = datetime.date.today()

    return render(request, 'index.html', {'description': description, 'icon': icon, 'temp': temp,
                                           'day': day,'error_message': error_message,'city': city})
