import requests

SHEETY_USER_ENDPOINT = 'https://api.sheety.co/f7b56028f361f38c336de6a4081683ef/flightDeals/users'  # noqa

print('Welcome to Flight Club\nWe find the best flight deals and email you.')
first_name = input('What is your first name?\n')
last_name = input('What is your last name?\n')
email = input('What is your email?\n')
email_validation = input('Type your email again.')
if email == email_validation:
    print('Welcome to flight club!')

    sheet_input = {
        'user': {
            'FirstName': first_name,
            'LastName': last_name,
            'Email': email
        }
    }

    sheet_response = requests.post(
        url=SHEETY_USER_ENDPOINT,
        json=sheet_input
    )

    print(sheet_response.text)
