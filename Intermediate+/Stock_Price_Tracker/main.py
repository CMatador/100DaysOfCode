# Day 36 - Stock Price Tracker (Extra Hard)

import requests
import datetime
from config import ALPHA_API_KEY, NEWS_API_KEY, account_sid, auth_token
from config import from_num, to_num
from twilio.rest import Client

STOCK = "AAPL"
COMPANY_NAME = "apple"


def last_weekday(date):
    date -= datetime.timedelta(days=1)
    while date.weekday() > 4:
        date -= datetime.timedelta(days=1)
    return date


def get_news():
    news_response = requests.get(
        url=news_endpoint,
        params=news_params
    )
    news_response.raise_for_status()
    news_data = news_response.json()
    news_text = ''

    for article in news_data['articles']:
        news_text += article['title'] + '\n'

    if percent_change >= 5:
        symbol = '🔺'
    else:
        symbol = '🔻'

    msg = f'{STOCK} {symbol} {percent_change}%\n{news_text}'
    return msg


today = datetime.datetime.now().date()
last_close_date = last_weekday(today)
second_date = last_weekday(last_close_date)

stock_endpoint = 'https://www.alphavantage.co/query'
stock_params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': ALPHA_API_KEY,
}

stock_response = requests.get(
    url=stock_endpoint,
    params=stock_params
)
stock_response.raise_for_status()

stock_data = stock_response.json()
last_close = \
    float(stock_data['Time Series (Daily)'][f'{last_close_date}']['4. close'])
second_close = \
    float(stock_data['Time Series (Daily)'][f'{second_date}']['4. close'])

percent_change = round(((last_close - second_close) / second_close) * 100)

news_endpoint = 'https://newsapi.org/v2/everything'
news_params = {
    'apiKEY': NEWS_API_KEY,
    'qInTitle': COMPANY_NAME,
    'pageSize': 3
}

if percent_change >= 5 or percent_change <= -5:
    sms_msg = get_news()
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=sms_msg,
        from_=from_num,
        to=to_num
    )
print(message.status)
