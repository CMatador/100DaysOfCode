# Day 33 - ISS Location Tracker

import requests
import datetime as dt
import smtplib
from config import my_email, password
import time

MY_LAT = 40.643501
MY_LONG = -74.076202


def is_close():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()

    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])

    if MY_LAT - 5 <= latitude <= MY_LAT + 5\
            and MY_LONG - 5 <= longitude <= MY_LONG + 5:
        return True


def is_dark():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0,
    }

    response = requests.get(
        url='https://api.sunrise-sunset.org/json',
        params=parameters
        )
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    if sunset <= current_hour <= sunrise:
        return True


time_now = dt.datetime.now()
current_hour = time_now.hour

while True:
    time.sleep(60)
    if is_close() and is_dark():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg='Subject:Look Up\n\n'
                'The ISS is nearby.'
            )
