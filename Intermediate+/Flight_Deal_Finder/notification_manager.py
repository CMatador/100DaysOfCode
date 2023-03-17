from twilio.rest import Client
from config import auth_token, account_sid, to_num, from_num


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=from_num,
            to=to_num
        )
        print(message.sid)
