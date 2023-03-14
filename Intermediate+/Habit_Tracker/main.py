# Day 37 - Habit Tracker

import requests
import datetime as dt
from config import USERNAME, TOKEN

GRAPH_ID = 'graph1'

# # Create User Account
pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(
#     url=pixela_endpoint,
#     json=user_params
# )

# Create Graph
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    'id': GRAPH_ID,
    'name': 'Python Coding Time',
    'unit': 'minutes',
    'type': 'int',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(
#     url=graph_endpoint,
#     json=graph_config,
#     headers=headers
# )

today = dt.datetime.now().date()
today_formatted = str(today.strftime('%Y%m%d'))

# Post Pixel
pixel_endpoint = f'{graph_endpoint}/{GRAPH_ID}'
pixel_params = {
    'date': '20230312',
    'quantity': '111'
}

# response = requests.post(
#     url=pixel_endpoint,
#     json=pixel_params,
#     headers=headers
# )

# Update Pixel
update_endpoint = f'{pixel_endpoint}/20230312'
update_params = {
    'quantity': '98'
}
# response = requests.put(
#     url=update_endpoint,
#     json=update_params,
#     headers=headers
# )

# Delete Pixel
response = requests.delete(
    url=update_endpoint,
    headers=headers
)

print(response.text)
