# Day 39/40 - Flight Deal Finder

import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = 'LON'

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

if sheet_data[0]['iataCode'] == '':
    city_names = [row['city'] for row in sheet_data]
    print(city_names)
    codes = flight_search.get_iatacode(city_names)
    data_manager.update_destination_code(codes)
    sheet_data = data_manager.get_destination_data()

destinations = {
    data['iataCode']: {
        'id': data['id'],
        'city': data['city'],
        'price': data['lowestPrice']
    } for data in sheet_data
}

tomorrow = dt.now() + dt.timedelta(days=1)
six_months = dt.now() + dt.timedelta(days=180)

for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_months
    )

    if flight is None:
        continue

    if flight.price < destinations[destination_code]:
        notification_manager.send_sms(
            message=f'Low price alert! Only £{flight.price} to fly from \
                {flight.origin_city}-{flight.origin_airport} to \
                    {flight.destination_city}-{flight.destination_airport},\
                        from {flight.out_date} to {flight.return_date}.'
        )
