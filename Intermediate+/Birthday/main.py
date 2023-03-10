# Day 32 - Automated Birthday Messages

# #################### Extra Hard Starting Project ######################

import datetime as dt
import pandas as pd
import random
import smtplib
from config import my_email, password

today = dt.datetime.now()
day = today.day
month = today.month

birthdays = pd.read_csv('Intermediate+/Birthday/birthdays.csv')

# Check dataframe to see if any dates match up to today's date
for index, row in birthdays.iterrows():
    if row['month'] == month and row['day'] == day:
        # Select a random letter template
        letter_path = f'Intermediate+/Birthday/letter_templates/\
letter_{random.randint(1, 3)}.txt'

        # Extracts text from letter template
        with open(letter_path) as file:
            letter_text = file.read()
        insert_name = letter_text.replace('[NAME]', row["name"])

        # Sends email to the person
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=f'{row["email"]}',
                msg='Subject:Happy Birthday!\n\n'
                f'{insert_name}'
            )
