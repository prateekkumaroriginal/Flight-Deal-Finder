from twilio.rest import Client

account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"


class NotificationManager:
    def __init__(self, message, from_mobile_number, to_mobile_number):
        self.message = message
        self.from_mobile_number = from_mobile_number
        self.to_mobile_number = to_mobile_number

    def send_message(self):
        client = Client(account_sid, auth_token)
        client.messages.create(
            body=self.message,
            from_=self.from_mobile_number,
            to=self.to_mobile_number
        )
