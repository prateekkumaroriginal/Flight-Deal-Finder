import requests

AUTH_TOKEN = "YOUR_SHEETY_AUTH_TOKEN"
auth_header = {
    'Authorization': AUTH_TOKEN
}
SHEETY_ENDPOINT = "https://api.sheety.co/2dc9cd05924e1a5bc77eb4f3a6902157/YOUR_SHEETY_PROJECT_NAME_IN_CAMEL_CASE"


class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.users = []

    def get_destination_data(self):
        response = requests.get(url=f"{SHEETY_ENDPOINT}/YOUR_SPREADSHEET_NAME_IN_CAMEL_CASE", headers=auth_header)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                'YOUR_SPREADSHEET_NAME_IN_CAMEL_CASE': {
                    'iataCode': city['iataCode']
                }
            }
            requests.put(url=f"{SHEETY_ENDPOINT}/YOUR_SPREADSHEET_NAME_IN_CAMEL_CASE/{city['id']}",
                         headers=auth_header,
                         json=new_data)

