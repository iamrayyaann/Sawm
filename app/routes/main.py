from flask import render_template, request, current_app
from datetime import datetime
import requests
from . import main

@main.route('/')
def home():
    
    # Get the IP Address of the user
    ip_address = request.remote_addr
    # ip_address = '8.8.8.8'
    
    # Get the City and Country of the user
    response = requests.get(f'https://geolocation-db.com/json/{ip_address}&position=true')
    print(response.json())  
    ip_data = response.json()
    city = ip_data.get('city', 'Unknown City')
    country = ip_data.get('country_name', 'Unknown Country')
    latitude = ip_data.get('latitude', 'N/A')
    longitude = ip_data.get('longitude', 'N/A')
    
    calc_method = '1'
    
    try:
        # response = requests.get(f'https://api.aladhan.com/timingsByAddress/{current_date}?address={city},{country}&method={calc_method}')
        # response_data = response.json()
        
        response = requests.get(f'https://api.aladhan.com/v1/timings?latitude={latitude}&longitude={longitude}&method={calc_method}')
        response_data = response.json()

        if response.status_code == 200 and response_data.get('data'):
            Suhoor = datetime.strptime(response_data['data']['timings']['Fajr'], '%H:%M').strftime('%I:%M %p')
            Iftar = datetime.strptime(response_data['data']['timings']['Maghrib'], '%H:%M').strftime('%I:%M %p')
        else:
            Suhoor = 'N/A'
            Iftar = 'N/A'
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f"API Request Error: {e}")
        Suhoor = 'N/A'
        Iftar = 'N/A'
    
    return render_template('home.html', Suhoor=Suhoor, Iftar=Iftar)

@main.route('/calendar')
def calendar():
    return render_template('calendar.html')

@main.route('/ramadan')
def ramadan():
    return render_template('ramadan.html')

@main.route('/settings')
def settings():
    return render_template('settings.html')