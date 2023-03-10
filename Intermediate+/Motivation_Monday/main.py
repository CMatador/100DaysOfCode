import smtplib
import datetime as dt
import random

from config import my_email, password

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open('Intermediate+/Birthday/quotes.txt') as file:
        quote_list = file.readlines()
        quote = random.choice(quote_list)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='rylovesjesse@yahoo.com',
            msg='Subject:Motivational Quote\n\n'
            f'{quote}'
        )
