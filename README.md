# Flight Deal Finder
This project consists of several Python files that work together to provide flight data and notifications for flight deals lower than your threshold.

## Note
To use it effectively, you should deploy it on a cloud service like Google's <a href="https://cloud.google.com/run/?userloc_9303169-network_g">Cloud Run</a>.

## Files
1. `flight_data.py`: Defines the FlightData class for storing flight data information.
2. `data_manager.py`: Contains the DataManager class for retrieving and updating destination data from an API.
3. `flight_search.py`: Implements the FlightSearch class for searching flights using an external API.
4. `notification_manager.py`: Defines the NotificationManager class for sending notifications via Twilio.
5. `main.py`: Contains the main program that utilizes the other files to search for low-priced flights and send notifications.

## Setup
1. Clone the repository or download all five Python files.
2. Install the required libraries using pip.
3. Obtain the necessary credentials:
- Obtain your `TEQUILA_API_KEY` from the Tequila API documentation or your account settings.
- `AUTH_TOKEN`: Replace it with your own <a href="https://sheety.co/">Sheety</a> Auth_Token.
- `account_sid = 'YOUR_TWILIO_ACCOUNT_SID'`<br>
- `auth_token = 'YOUR_TWILIO_AUTH_TOKEN'`<br>
- `from_='+YOUR_TWILIO_PHONE_NUMBER'`
- `to='+YOUR_DESTINATION_PHONE_NUMBER'`

## Usage
1. Run the `main.py` Python script in your terminal or IDE.
2. The project will retrieve the latest flight deals' data for the specified destination and other details using the `Tequila` API.
3. It will compare the prices with the threshold prices saved in the google spreadsheet.
![Screenshot (333)](https://github.com/prateekkumaroriginal/Flight-Deal-Finder/assets/89418989/dd23735c-1758-416d-b8e3-b57d9b395393)

4. If the price is lower than the threshold, it will fetch relevant details and send a sms using `Twilio`.
5. Check your phone for the received SMS alert.

## Tech Stack
Language: Python <br>
Libraries: `requests`, `twilio`, `datetime`

## API's 
<a href="https://tequila.kiwi.com/portal/getting-started">Tequila</a> - To find flight deals. <br>
<a href="https://sheety.co/">Sheety</a> - To store and update flight details. <br>
<a href="https://www.twilio.com/docs/sms">Twilio</a> - To send SMS notifications.
