from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime as dt

flight_search = FlightSearch()

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

for row in sheet_data:
    if row['iataCode'] == "":
        row['iataCode'] = flight_search.get_destination_code(row['city'])

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

tomorrow = dt.datetime.now() + dt.timedelta(days=1)
six_months_from_today = dt.datetime.now() + dt.timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        "LON",
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )

    if flight.price <= destination['maxPrice']:
        message = f"Low Price Alert! Only {flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to" \
                  f"{flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
        notification_manager = NotificationManager(message=message,
                                                   from_mobile_number=YOUR_TWILIO_PHONE_NUMBER,
                                                   to_mobile_number=YOUR_DESTINATION_PHONE_NUMBER)
        notification_manager.send_message()
