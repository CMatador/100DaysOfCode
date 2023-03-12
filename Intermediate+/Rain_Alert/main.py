# Day 35 - Rain Alert

import requests
from config import API_KEY, account_sid, auth_token, from_num, to_num
from twilio.rest import Client

MY_LAT = 40.643501
MY_LONG = -74.076202

parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}

response = requests.get(
    url='https://api.openweathermap.org/data/2.8/onecall',
    params=parameters
)
response.raise_for_status()

weather_data = response.json()
will_rain = False

# weather condition codes for next 12 hours
for i in range(12):
    code = int(weather_data['hourly'][i-1]['weather'][0]['id'])
    if code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Here's Ollie with the forecast:\nIT'S GON RAIN!",
        from_=from_num,
        to=to_num
    )
    print(message.status)
