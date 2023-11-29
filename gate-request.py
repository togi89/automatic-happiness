import requests


flight_number_input = input('Please input flight number, including airline ICAO code: ')
flight_number_airline = flight_number_input[0:3]
flight_number = flight_number_input[3:]

params = {
  'access_key': 'd18ef61b40fe5068a409fb62ef17ac71',
  'flight_number': flight_number,
  'airline_icao': flight_number_airline,
  'limit': 1,
}

api_result = requests.get('http://api.aviationstack.com/v1/flights', params)


api_response = api_result.json()

flight = api_response["data"][0]

print(f'{flight["flight"]["icao"]} Details \n')
print('Departing %s || terminal %s, gate %s' % (flight["departure"]["airport"], flight["departure"]["terminal"], flight["departure"]["gate"])) 
# for flight in api_response['data']:
#     print(flight['flight_date'], flight['departure']['gate'])
#     print(flight['flight_date'], flight['arrival']['gate'])
# if api_response is False:
#     print("maybe try a 0 infront of the flight number?")


""" 2023-11-12 

{'airport': 'Honolulu International', 'timezone': 'Pacific/Honolulu', 'iata': 'HNL', 'icao': 'PHNL', 'terminal': '1', 'gate': 'A19', 'delay': None, 'scheduled': '2023-11-12T15:30:00+00:00', 'estimated': '2023-11-12T15:30:00+00:00', 'actual': None, 'estimated_runway': None, 'actual_runway': None} """

# {'flight_date': '2023-11-11',
#  'flight_status': 'landed',
#  'departure': 
#  {'airport': 'Honolulu International', 'timezone': 'Pacific/Honolulu', 'iata': 'HNL', 'icao': 'PHNL', 'terminal': '1', 'gate': 'A19', 'delay': 2, 'scheduled': '2023-11-11T15:30:00+00:00', 'estimated': '2023-11-11T15:30:00+00:00', 'actual': '2023-11-11T15:31:00+00:00', 'estimated_runway': '2023-11-11T15:31:00+00:00', 'actual_runway': '2023-11-11T15:31:00+00:00'}, 
#  'arrival': {'airport': 'Kona International Airport', 'timezone': 'Pacific/Honolulu', 'iata': 'KOA', 'icao': 'PHKO', 'terminal': '2', 'gate': '9', 'baggage': None, 'delay': None, 'scheduled': '2023-11-11T16:18:00+00:00', 'estimated': '2023-11-11T16:18:00+00:00', 'actual': '2023-11-11T16:01:00+00:00', 'estimated_runway': '2023-11-11T16:01:00+00:00', 'actual_runway': '2023-11-11T16:01:00+00:00'}, 'airline': {'name': 'Hawaiian Airlines', 'iata': 'HA', 'icao': 'HAL'}, 'flight': {'number': '368', 'iata': 'HA368', 'icao': 'HAL368', 'codeshared': None}, 'aircraft': None, 'live': None}