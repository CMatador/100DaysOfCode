import requests

SHEETY_ENDPOINT = 'https://api.sheety.co/f7b56028f361f38c336de6a4081683ef/flightDeals/prices'  # noqa


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(
            url=SHEETY_ENDPOINT
        )
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(
                url=f'{SHEETY_ENDPOINT}/{city["id"]}',
                json=new_data
            )
            print(response.text)
