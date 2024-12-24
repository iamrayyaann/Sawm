from flask import render_template, current_app
from datetime import datetime
import requests
from . import main

@main.route('/')
def home():
    current_date = datetime.now().strftime('%d-%m-%Y')
    calc_method = '1'
    city = 'Bangalore'
    country = 'India'
    try:
        response = requests.get(f'https://api.aladhan.com/timingsByAddress/{current_date}?address={city},{country}&method={calc_method}')
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