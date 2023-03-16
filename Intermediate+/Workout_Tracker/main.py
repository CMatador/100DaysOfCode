# Day 38 - Workout Tracker

from config import APP_ID, API_KEY, SHEETY_TOKEN
import requests
import datetime as dt

GENDER = 'male'
WEIGHT = 122.4
HEIGHT = 188
AGE = 36

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/f7b56028f361f38c336de6a4081683ef/\
    workoutTracking/workouts'

exercise = input('What exercise did you do: ')

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

params = {
    'query': exercise,
    'gender': GENDER,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE
}

response = requests.post(
    url=exercise_endpoint,
    json=params,
    headers=headers
)
response.raise_for_status()
result = response.json()


current_time = dt.datetime.now()
date_now = current_time.strftime('%x')
time_now = current_time.strftime('%X')

for exercise in result['exercises']:
    sheet_input = {
        'workout': {
            'date': date_now,
            'time': time_now,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

sheet_header = {
    'Authorization': f'Bearer {SHEETY_TOKEN}'
}

sheet_response = requests.post(
    url=sheety_endpoint,
    json=sheet_input,
    headers=sheet_header
)

print(sheet_response.text)
